#!/usr/bin/node
const dict = require('./101-data').dict;
const sortedDict = {};
for (const key in dict) {
  (dict[key] in sortedDict) ? sortedDict[dict[key]].push(key) : sortedDict[dict[key]] = Array(key);
}
console.log(sortedDict);
