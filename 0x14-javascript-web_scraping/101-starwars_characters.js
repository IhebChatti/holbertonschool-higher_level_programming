#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let result = [];
request.get(url, (error, respponse, body) => {
  (error) ? console.log(error) : result = JSON.parse(body).characters;
  for (const charId in result) {
    const orderedNames = {};
    request.get(result[charId], (error, response, body) => {
      (error) ? console.log(error) : orderedNames[charId] = JSON.parse(body).name;
      if (Object.keys(result) !== Object.keys(orderedNames)) {
        console.log(orderedNames[charId]);
      }
    });
  }
});
