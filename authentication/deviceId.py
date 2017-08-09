from hashlib import sha1

def getDeviceId(steamId):
    s = sha1(str(steamId).encode('UTF-8')).hexdigest()  # Encode SteamId to UTF-8 and then hash it with SHA1 algorithm
    n = [8, 4, 4, 4, 12]  # Certain splitting pattern for Android's Device Id's
    return "android:" + '-'.join([s[sum(n[:i]): sum(n[:i + 1])] for i in range(len(n))])

