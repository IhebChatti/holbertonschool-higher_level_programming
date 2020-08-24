#!/usr/bin/python3
"""[Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.]
"""
import requests
from sys import argv
if __name__ == "__main__":
    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""
    value = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, value)
    try:
        json_data = r.json()
        elif json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
    except:
        print("Not a valid JSON")
