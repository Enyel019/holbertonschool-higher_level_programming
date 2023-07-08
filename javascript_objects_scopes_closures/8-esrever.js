#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const newlist = [];
  for (let i = len - 1; i >= 0; i--) {
    newlist.push(list[i]);
  }
  return newlist;
};
