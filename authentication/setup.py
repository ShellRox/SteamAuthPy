from deviceId import *
from oauth import *
from guard import *
import time
import json
from binascii import unhexlify
import requests
import hashlib
import os

class AddAuthenticator(object):

    def registerAuthenticator(self, steamId, Oauth, UDID):

        req = requests.post("https://api.steampowered.com/ITwoFactorService/AddAuthenticator/v1/?key=AFC007D4145C90CC836E48A5FC68264A/", data={
            "steamid": str(steamId),  # Your SteamID64
            "access_token": str(Oauth),  # Oauth (Access) token
            "authenticator_time": int(time.time()),  # Time in microseconds
            "authenticator_type": 1,  # ValveMobileApp
            "device_identifier": str(UDID),  # Your device Id here
            "sms_phone_id": "1"})  # 1 = Your caller id

        conf = raw_input("Enter the confirmation code: ")

        return self.finalize(req.json(), str(conf), str(steamId), str(Oauth))

    def finalize(self, secret_json, code, steamId, Oauth, logging=True):
        s = secret_json
        sguard = SteamGuard()
        r = requests.post("https://api.steampowered.com/ITwoFactorService/FinalizeAddAuthenticator/v1/", data={
            "steamid": str(steamId),
            "access_token": str(Oauth),
            "authenticator_code": sguard.get_confirmation_key(int(time.time()), s.get('response').get('shared_secret')),
            "authenticator_time": int(time.time()),
            "activation_code": code,
        })

        print(r.json())

        if (int(r.status_code) == 200):
            secret_response = s
            if logging:
                new_log = {str(steamId): str(secret_response)}
                with open(os.path.join(os.path.dirname(__file__), 'shared_secrets.json')) as d:
                    data = json.load(d)
                data.update(new_log)
                with open(os.path.join(os.path.dirname(__file__), 'shared_secrets.json'), 'w') as d:
                    json.dump(data, d)

            return secret_response
        else:
            raise ValueError("Couldn't register authenticator. Status: {0}".format(int(r.status_code)))
