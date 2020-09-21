#!/usr/bin/node
const dict = require('./101-data').dict;
const new_dict = {};
for (const key in dict) {
  (dict[key] in new_dict) ? new_dict[dict[key]].push(key) : new_dict[dict[key]] = Array(key);
}
console.log(new_dict);
