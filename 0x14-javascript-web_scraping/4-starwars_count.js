#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let result = [];
request.get(url, (error, respponse, body) => {
  (error) ? console.log(error) : result = JSON.parse(body).results;
  let count = 0;
  for (const movie in result) {
    const characters = result[movie].characters;
    for (const char in characters) {
      if (characters[char].endsWith('/18/')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
