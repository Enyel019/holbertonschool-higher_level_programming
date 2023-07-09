#!/usr/bin/node
const url = 'http://swapi.co/api/films/' + process.argv[2];
const request = require('request');

request.get(url, function (err, response, body) {
  if (err) {
    return console.log(err.toString());
  }
  console.log(JSON.parse(body).title);
});
