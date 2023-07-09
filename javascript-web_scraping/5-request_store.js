#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const urlPath = process.argv[2];
const filePath = process.argv[3];

request(urlPath, function (err, res, body) {
  if (err) {
    throw (err);
  }

  const text = body;

  fs.writeFile(filePath, text, 'utf-8', (err) => {
    if (err) {
      throw err;
    }
  });
});
