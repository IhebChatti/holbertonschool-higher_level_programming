#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let chars;
const ordNames = {};
request.get(url, (error, respponse, body) => {
  (error) ? console.log(error) : chars = JSON.parse(body).characters;
  for (const id of chars) {
    request.get(id, (error, response, body) => {
      if (!error) {
        ordNames[id] = JSON.parse(body).name;
        if (Object.values(ordNames).length === chars.length) {
          for (const id of chars) {
            console.log(ordNames[id]);
          }
        }
      }
    });
  }
});
