#!/usr/bin/python3
""" sends a POST request to the passed URL with email as parameter """
import sys
import urllib.request
import urllib.parse

data = sys.argv[2]
""" data = urllib.parse.urlencode(email)"""
data = data.encode('ascii')
req = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(req) as response:
    email_resp = response.read().decode('utf-8')
    print("Your email is: {}".format(email_resp))
