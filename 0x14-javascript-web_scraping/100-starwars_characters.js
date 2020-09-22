#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let result = [];
request.get(url, (error, respponse, body) => {
  (error) ? console.log(error) : result = JSON.parse(body).characters;
  for (const charId in result) {
    request.get(result[charId], (error, response, body) => {
      (error) ? console.log(error) : console.log(JSON.parse(body).name);
    });
  }
});
