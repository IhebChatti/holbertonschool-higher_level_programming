#!/usr/bin/python3
"""[Python script that takes in 3 strings
    and sends a search request to the Twitter API]
"""
import base64
from sys import argv
import requests
if __name__ == "__main__":
    api_key = argv[1]
    api_secret = argv[2]
    string = argv[3]
    key_secret = '{}:{}'.format(api_key, api_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')
    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)

    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {
        'grant_type': 'client_credentials'
    }

    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    access_token = auth_resp.json().get('access_token')
    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    search_params = {
        'q': string,
        'result_type': 'recent',
        'count': 5
    }
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    search_resp = requests.get(search_url, headers=search_headers,
                               params=search_params).json().get('statuses')
    for values in search_resp:
        print("[{}] {} by {}".format(values.get('id'),
                                     values.get('text'),
                                     values.get('user').get('name')))
