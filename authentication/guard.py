import time
from binascii import unhexlify
import requests
import hmac
import base64
import hashlib
import struct
import ctypes

class SteamGuard(object):
    def long_to_bytes(self, val, endianness='big'):
        width = 64
        fmt = '%%0%dx' % (width // 4)  # Format to number to bytes
        s = unhexlify(fmt % val)  # Binary data from hexadecimal number
        if (endianness == 'little'):  # In most cases, This boolean operation is not significant.
            s = s[::-1]
        return s

    def get_server_time(self):
        r = requests.post('https://api.steampowered.com/ITwoFactorService/QueryTime/v1')
        jsn = r.json()
        return jsn.get('response').get('server_time')

    def get_auth_code(self, tm, secret, *tag):
        STEAM_CHARS = ['2',  # Official Steam characters, Works with ValveMobileApp
                       '3',
                       '4',
                       '5',
                       '6',
                       '7',
                       '8',
                       '9',
                       'B',
                       'C',
                       'D',
                       'F',
                       'G',
                       'H',
                       'J',
                       'K',
                       'M',
                       'N',
                       'P',
                       'Q',
                       'R',
                       'T',
                       'V',
                       'W',
                       'X',
                       'Y']
        def toLong(x): return long(x.encode('hex'), 16)  # Hexlify integer and convert it to long as hexadecimal (radix 16)
        def local(): return long(round(time.mktime(time.localtime(time.time())) * 1000))  # Exact time converted to seconds
        timediff = local() - (long(self.get_server_time()) * 1000)  # Time difference between steam server and machine
        def codeinterval(): return long((local() + timediff) / 30000)  # Code interval between steam server and machine
        v = self.long_to_bytes(val=codeinterval())  # Convert long integer to bytes
        if len(tag) > 0:
            v += tag[0]
        h = hmac.new(base64.b64decode(secret), v, hashlib.sha1)  # Decode shared secret and then create hmac for $v
        digest = h.digest()
        start = toLong(digest[19]) & 0x0f  # Bitwse <AND> operation between long hexadecimal number and 15 (0x0f)
        b = digest[start:start + 4]  # Unfiltered code
        fullcode = toLong(b) & 0x7fffffff  # Unfiltered full code as long integer
        CODE_LENGTH = 5
        code = ''
        for i in range(CODE_LENGTH):
            code += STEAM_CHARS[fullcode % len(STEAM_CHARS)]  # Filtering code with steam characters
            fullcode /= len(STEAM_CHARS)  # Filtered full code as long integer (Divided by 26)
        return code

    def get_confirmation_key(self, tm, secret, tag):
        _buffer = struct.pack('>Q', tm) + tag.encode('ascii')
        return base64.b64encode(hmac.new(base64.b64decode(secret), _buffer, digestmod=hashlib.sha1).digest())

    def old_get_confirmation_key(self, tm, secret, tag):
        identity_secret = self.BufferizeSecret(str(secret))
        datalen = 8
        if (tag):
            if (len(tag) > 32):
                datalen += 32
            else:
                datalen += len(tag)
        _buffer = ctypes.create_string_buffer(datalen)  # Create empty byte array to fill
        timestamp = tm
        struct.pack_into(">i", _buffer, 4, int(timestamp))  # Write current unix time as UInt32 to our byte array
        if (tag):
            for c in list("conf"):
                struct.pack_into(">c", _buffer, 8 + (list("conf").index(c)), c)  # We write tag name as char to buffer
        _hmac = hmac.new(identity_secret, _buffer, hashlib.sha1)  # Create SHA-1 hmac
        return base64.b64encode(_hmac.digest())  # Return base64 digest

    def get_time_offset(self):
        offset = int(float(self.get_server_time()) - time.time())
        return offset

    @staticmethod
    def BufferizeSecret(secret):
        if isinstance(secret, str):  # Check for string instance
            try:  # Check if secret is hexadecimal
                int(secret, 16)
            except ValueError:
                #  We assume that our secret key is in Base64 format if it's not in hexadecimal. In this case, we get
                #  byte array after decoding secret from Base64.
                return base64.b64decode(str(secret))
            else:
                # If our secret key is in hexadecimal format, We get our Buffer by making proper list from our byte
                # array which was derived from decoding our hexadecimal format secret key.
                return str(secret).decode('hex')


s = SteamGuard()
