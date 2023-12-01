#!/usr/bin/python3
""" uses the GitHub API to display your id """
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    git_usrname = sys.argv[1]
    git_pass_token = sys.argv[2]

    auth = HTTPBasicAuth(git_usrname, git_pass_token)
    req = requests.get("https://api.github.com/user", auth=auth)

    info = req.json()
    user_id = info.get('id')
    print(user_id)
