#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduce((a, b) => [b].concat(a), []);
};
