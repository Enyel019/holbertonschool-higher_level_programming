#!/usr/bin/node
const movieNumber = process.argv[2];
const urlPath = 'https://swapi-api.hbtn.io/api/films/' + movieNumber;
const request = require('request');

request(urlPath, function (err, res, body) {
  if (err) {
    throw (err);
  }
  console.log(JSON.parse(body).title);
});
