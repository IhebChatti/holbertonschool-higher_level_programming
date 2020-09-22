#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(url, (error, response, body) => {
  (error) ? console.log(error) : console.log(JSON.parse(body).title);
});
