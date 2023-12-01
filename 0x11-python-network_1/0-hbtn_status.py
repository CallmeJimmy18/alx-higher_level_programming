#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as a_response:
        fle = a_response.read()
        print("Body response:")
        print("\t - type:", type(fle))
        print("\t- content:", format(fle))
        print("\t- utf8 content:", fle.decode('utf-8'))
