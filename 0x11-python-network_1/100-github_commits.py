#!/usr/bin/python3
"""[Python script that takes your Github credentials (username
    and password) and uses the Github API to display your id]
"""
import requests
from sys import argv
if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    req = requests.get(url)
    data = req.json()
    for i in range(10):
        j = 0
        if j >= 10:
            break
        print("{}: {}".format(data[i].get("sha"), data[i].get(
            "commit").get("author").get("name")))
