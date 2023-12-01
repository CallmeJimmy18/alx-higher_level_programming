#!/usr/bin/python3
""" POST request to http://0.0.0.0:5000/search_user with the letter """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1 and isinstance(sys.argv[1], str):
        q = sys.argv[1]
    else:
        q = ""

    data_to_in = {'q': q}
    req = requests.post('http://0.0.0.0:5000/search_user', data_to_in)
    data = req.json()
    
    if data and isinstance(data, dict):
        data_id = data["id"]
        data_name = data["name"]
        print("[{}] {}".format(data_id, data_name))
    elif not data:
        print("No result")
    elif not isinstance(data, dict):
        print("Not a valid JSON")
