#!/usr/bin/node
const urlPath = process.argv[2];
const request = require('request');
let count = 0;

request(urlPath, function (err, res, body) {
  if (err) {
    throw (err);
  }

  const movies = JSON.parse(body);
  movies.results.forEach(movie => {
    movie.characters.forEach(character => {
      if (character.includes('18')) {
        count++;
      }
    });
  });

  console.log(count);
});
