#!/usr/bin/python3
""" sends a POST request to the passed URL with email as parameter """
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        email_resp = response.read().decode('utf-8')
        print(email_resp)
