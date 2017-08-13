# SteamAuthPy
Simple module to authenticate on Steam website with Python 2

**This module only supports Python 2.7-2.6 versions, If you use Python 3, Please use [steampy](https://github.com/bukson/steampy) (We are not associated in any way with steampy).**

# Install
You can install this module using Python's official package manager:
`pip install SteamAuthPy`

To easily use this module, Simply define the instance of called `Request` object:

```python
from SteamLoginPy.setup.main import Request
import time
r = Request()
print(r.requestConfKey(time.time(), "caOdv/kdRloP9nbh3gMkxKaXALI=", "conf"))
```
---
# requestGuide()

Returns a string of information about all functions in controller and arguments that they take.

# requestOauth(*path)

Uses regex to find Oauth (Access) token from Steam's chat. If path argument is not entered, `authentication/steamchat.html` is checked.

You are required to copy HTML like this in order for module to work:

1. Access http://steamcommunity.com/chat
2. Inspect elements (If you are on Google Chrome, right click and inspect)
3. Copy OuterHTML of body:
![Copying OuterHTML on Chrome](http://i.imgur.com/o85L6uy.png)
4. Paste OuterHTML in steamchat.html
5. Call the function

# requestDeviceId(steamId)

Returns generated working Android's UDID by your SteamID64.

# requestSetup(steamId, Oauth, UDID, logging=True)

Add Steam's mobile authenticator on your account.

If logging argument is False, Json response which contains important data (e.g shared_secret & identity_secret) will not be logged in `shared_secrets.json` file. Please change this argument only if you are 100% sure that you will save this data manually.

# requestSecrets()

Returns decoded Json of file containing all information that was logged when executing requestSetup function.

# requestAuthCode(time, shared_secret)

Returns generated Two-factor authentication code from time and shared_secret.

# requestConfKey(time, identity_secret, tag)

Returns generated trade offer confirmation key from time, identity secret and tag name.

# requestLogin(username, password, shared_secret)

Returns a requests session containing all cookies obtained from Authentication (In short, It returns login session if correct arguments are passed).

