import re
import os
def finder(path="steamchat.html"):
    source = open(str(os.path.join(os.path.dirname(__file__), path)), "r")
    string = str(source.read())
    query = re.findall('access_token=(\w{32})', string)
    if len(query) < 1:
        raise ValueError("Incorrect OuterHTML")
    else:
        return str(query[0])
