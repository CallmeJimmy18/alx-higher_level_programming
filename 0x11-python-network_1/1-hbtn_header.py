#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in the header """
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        req_id = response.headers.get('X-Request-Id')
        print(req_id)
