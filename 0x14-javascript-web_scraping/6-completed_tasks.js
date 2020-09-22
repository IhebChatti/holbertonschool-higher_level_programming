#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let todos;
const doneTasks = {};
request.get(url, (error, response, body) => {
  (error) ? console.log(error) : todos = JSON.parse(body);
  for (const i in todos) {
    const todo = todos[i];
    if (todo.completed === true) {
      if (!doneTasks[todo.userId]) {
        doneTasks[todo.userId] = 1;
      } else {
        doneTasks[todo.userId]++;
      }
    }
  }
  console.log(doneTasks);
});
