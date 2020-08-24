#!/usr/bin/python3
"""[Python script that takes in a URL, sends a request to
    the URL and displays the body of the response]
"""
from urllib import request
import urllib.parse
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("ascii"))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
