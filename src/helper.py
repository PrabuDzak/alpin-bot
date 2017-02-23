import re

def extract_command(str):
    s = str.lower()
    s = re.search("pin (.*) pin", s)
    if (s is not None):
        return s.group(1)
    else:
        return ""
