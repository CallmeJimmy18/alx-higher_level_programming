#!/usr/bin/python3
""" If the HTTP status code is >= 400, print: Error code: """
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)
