#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((accumulator, elements) => {
    return (searchElement === elements ? accumulator + 1 : accumulator);
  }, 0);
};
