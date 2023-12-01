#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as a_response:
        fle = a_response.read()
        print("Body response:")
        print("    - type: {}".format(type(fle)))
        print("    - content: {}".format(fle))
        print("    - utf8 content: {}".format(fle.decode('utf-8')))
