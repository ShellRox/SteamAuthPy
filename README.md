# SteamAuthPy
Simple module to authenticate on Steam website with Python 2

**This module only supports Python 2.7-2.6 versions, If you use Python 3, Please use [steampy](https://github.com/bukson/steampy) (We are not associated in any way with steampy).**

# Installation

You can install ths module with pip:

`pip install SteamAuthPy`

# Methods

*Example*

```python
import SteamAuthPy
import time
print(SteamAuthPy.confkey(time.time(), "caOdv/kdRloP9nbh3gMkxKaXALI=", "conf"))
```

# guide()

Returns a string of information about all functions in controller and arguments that they take.

# oauth(*path)

`*path` - Path to the Steam Chat's HTML file

Uses regex to find Oauth (Access) token from Steam's chat. If path argument is not entered, `authentication/steamchat.html` is checked.

You are required to copy HTML like this in order for module to work:

1. Access http://steamcommunity.com/chat
2. Inspect elements (If you are on Google Chrome, right click and inspect)
3. Copy OuterHTML of body:
![Copying OuterHTML on Chrome](http://i.imgur.com/o85L6uy.png)
4. Paste OuterHTML in steamchat.html
5. Call the function

# deviceid(steamId)

`steamId` - SteamID64 (String)

Returns generated working Android's UDID by your SteamID64.

# setup(steamId, Oauth, UDID, logging=True)

`steamId` - SteamID64 (String);

`Oauth` - Access Token (String);

`UDID` - Unique Device Identifier (device id) (String);

`logging` - Boolean value (True/False);


Add Steam's mobile authenticator on your account.

If logging argument is False, Json response which contains important data (e.g shared_secret & identity_secret) will not be logged in `shared_secrets.json` file. Please change this argument only if you are 100% sure that you will save this data manually.

# secrets()

Returns decoded Json of file containing authenticator response information if it was logged

# authcode(time, shared_secret)

`time` - Unix time (Should be current time in most of the cases);

`shared_secret` - Shared secret key;

Returns generated Two-factor authentication code from time and shared_secret.

# confkey(time, identity_secret, tag)

`time` - Unix time (Should be current time in most of the cases);

`identity-secret` - Identity secret key;

`tag` - Tag that should be added to bytearray;

Returns generated trade offer confirmation key from time, identity secret and tag name.

# login(username, password, shared_secret)

`username` - Username of your Steam account;

`password` - Password of your Steam account;

`shared_secret` - Shared secret key;

Returns a requests session containing all cookies obtained from Authentication (In short, It returns login session if correct arguments are passed).

