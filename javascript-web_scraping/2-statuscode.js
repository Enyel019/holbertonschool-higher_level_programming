#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url)
  .on('response', function (response) {
    console.log('code: %s', response.statusCode.toString());
  });
