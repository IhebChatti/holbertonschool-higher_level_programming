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

  headers: {
    Authorization: 'Basic ' + encodedKey,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  },

  form: {
    grant_type: 'client_credentials'
  }
};

let accessToken;
request.post(authParams, (error, response, body) => {
  (error) ? console.log(error) : accessToken = JSON.parse(body).access_token;
  search(accessToken);
});

const search = (accessToken) => {
  const searchParams = {
    url: baseURL + '1.1/search/tweets.json',

    headers: {
      Authorization: 'Bearer ' + accessToken
    },

    qs: {
      q: searchString,
      count: 5
    }
  };

  request.get(searchParams, (error, response, body) => {
    if (!error) {
      for (const tweet of JSON.parse(body).statuses) {
        console.log('[' + tweet.id + ']' + tweet.text + ' by ' + tweet.user.name);
      }
    }
  });
};
