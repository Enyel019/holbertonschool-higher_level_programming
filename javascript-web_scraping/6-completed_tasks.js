#!/usr/bin/node
const urlPath = process.argv[2];
const request = require('request');
const complete = {};

request(urlPath, (err, res, body) => {
  if (err) {
    throw (err);
  }
  const ans = JSON.parse(body);
  ans.forEach(task => {
    if (task.completed) {
      const user = task.userId;
      if (user in complete) {
        complete[user]++;
      } else {
        complete[user] = 1;
      }
    }
  });
  console.log(complete);
});
