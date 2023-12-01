#!/usr/bin/python3
""" displays the value of the variable X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1], auth=('user', 'pass'))
    print(req.headers['X-Request-Id'])
