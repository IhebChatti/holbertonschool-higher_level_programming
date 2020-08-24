#!/usr/bin/python3
"""[sumPython script that fetches
    https://intranet.hbtn.io/statusmary]
"""
import requests
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    req = req.text
    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format(req))
