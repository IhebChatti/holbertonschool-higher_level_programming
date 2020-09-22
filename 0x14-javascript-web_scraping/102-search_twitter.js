#!/usr/bin/node
const request = require('request');
const base64 = require('base-64');
const utf8 = require('utf8');

const APIkey = process.argv[2];
const APIsecret = process.argv[3];
const searchString = process.argv[4];
const keySecret = APIkey + ':' + APIsecret;
const encodedKey = base64.encode(keySecret);
utf8.decode(encodedKey);
const baseURL = 'https://api.twitter.com/';
const authParams = {
  url: baseURL + 'oauth2/token',

  auth_headers: {
    Authorization: 'Basic ' + encodedKey,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  },

  auth_data: {
    grant_type: 'client_credentials'
  }
};

let accessToken;
request.post(authParams, (error, response, body) => {
  (error) ? console.log(error) : accessToken = JSON.parse(body).accessToken;
});
const searchParams = {
  url: baseURL + '1.1/search/tweets.json',

  search_headers: {
    Authorization: 'Bearer ' + accessToken
  },

  search_params: {
    q: searchString,
    count: 5
  }
};

request.get(searchParams, (error, response, body) => {
  let tweets;
  (error) ? console.log(error) : tweets = JSON.parse(body).statuses;
  for (const tweet in tweets) {
    console.log(JSON.parse(tweet));
    console.log('[' + JSON.parse(tweet).id + ']' + JSON.parse(tweet).text + 'by' + JSON.parse(tweet).name);
  }
});
