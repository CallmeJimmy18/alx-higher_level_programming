#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status',
                       auth=('user', 'pass'))
    print("Body response:")
    print("    - type:", type(req.text))
    print("    - content:", req.text)
