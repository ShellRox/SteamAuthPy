from authentication.oauth import finder
from authentication.setup import AddAuthenticator
from authentication.deviceId import getDeviceId
from authentication.guard import SteamGuard
from authentication.login import Login
import json

def guide(self):
    print(
        """
        All Functions:
            
            Show guide - requestGuide();\n                       
            Get access token - requestOauth(*path);\n          
            Generate device id - requestDeviceId(steamid);\n           
            Add authenticator - requestSetup(steamid, access_token, device id);\n
            List logged secret keys - requestSecrets();\n
            Generate two-factor authentication code - requestAuthCode(time, secret_key);\n
            Generate trade offer confirmation key - requestConfKey(time, secret_key, tag_name);\n
            Send login request - requestLogin(username, password, secret_key);\n
            
        """
    )
def oauth(*p):
    if len(p) < 1:
        finder(path="authentication/steamchat.html")
    else:
        finder(path=str(p))

def deviceid(steamid):
    if len(str(steamid)) == 17 and str(steamid).isdigit():
        return getDeviceId(str(steamid))
    else:
        raise ValueError("Please enter proper steamId")

def setup(steamId, Oauth, UDID, logging=True):
    if len(str(steamId)) == 17 and str(steamId).isdigit():
        addAuth = AddAuthenticator()
        return addAuth.registerAuthenticator(steamId, Oauth, UDID)
    else:
        raise ValueError("Please enter proper steamId")

def secrets(self):
    with open('authentication/shared_secrets.json', 'r') as data:
        return json.load(data)

def authcode(secret):
    obj = SteamGuard()
    return obj.get_auth_code(int(tm), str(secret))

def confkey(secret, tag):
    obj = SteamGuard()
    return obj.get_confirmation_key(int(tm), str(secret), tag)

def login(username, password, shared_secret):
    _login = Login(str(username), str(password), str(shared_secret))
    return _login.getInfo()

