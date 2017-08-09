from authentication.oauth import finder
from authentication.setup import AddAuthenticator
from authentication.deviceId import getDeviceId
from authentication.guard import SteamGuard
from authentication.login import Login
import json

class Request(object):
    def requestGuide(self):
        print(
            """
            All Functions:
                
                Show guide - requestGuide();\n                       
                Get access token - requestOauth(*path);\n          
                Generate device id - requestDeviceId(steamid);\n           
                Add authenticator - requestSetup(steamid, access_token, device id);\n
                List logged secret keys - requestSecrets();\n
                Generate two-factor authentication code - requestCode(time, secret_key);\n
                Send login request - requestLogin(username, password, secret_key);\n
                
            """
        )
    def requestOauth(*p):
        if len(p) < 1:
            finder(path="authentication/steamchat.html")
        else:
            finder(path=str(p))

    def requestDeviceId(self, steamid):
        if len(str(steamid)) == 17 and str(steamid).isdigit():
            return getDeviceId(str(steamid))
        else:
            raise ValueError("Please enter proper steamId")

    def requestSetup(self, steamId, Oauth, UDID, logging=True):
        if len(str(steamId)) == 17 and str(steamId).isdigit():
            addAuth = AddAuthenticator()
            return addAuth.registerAuthenticator(steamId, Oauth, UDID)
        else:
            raise ValueError("Please enter proper steamId")

    def requestSecrets(self):
        with open('authentication/shared_secrets.json', 'r') as data:
            return json.load(data)

    def requestCode(self, tm, secret):
        obj = SteamGuard()
        return obj.get_confirmation_key(tm, str(secret))

    def requestLogin(self, username, password, shared_secret):
        login = Login(str(username), str(password), str(shared_secret))
        return login.getInfo()

