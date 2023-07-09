#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request(url, function (err, res, body) {
  if (err) {
    throw (err);
  }
  console.log('code: ${res.statusCode}');
});
