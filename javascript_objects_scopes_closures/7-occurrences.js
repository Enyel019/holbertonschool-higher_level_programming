#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let found = 0;
  for (let i = 0; i < len; i++) {
    if (searchElement === list[i]) {
      found += 1;
    }
  }
  return found;
};
