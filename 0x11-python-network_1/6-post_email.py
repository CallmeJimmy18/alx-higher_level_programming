#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """
import requests
import sys

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], email)
    print(req.text)
