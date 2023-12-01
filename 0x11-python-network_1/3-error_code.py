#!/usr/bin/python3
""" manage urllib.error.HTTPError exceptions and print: Error code: """
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print('Error code:', error.code)
