#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];
let result;
request.get(url, (error, respponse, body) => {
  (error) ? console.log(error) : result = body;
  fs.writeFile(fileName, result, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
