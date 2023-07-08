#!/usr/bin/node
let printed = 0;

exports.logMe = function (item) {
  console.log('%i: %s', printed, item);
  printed += 1;
};
