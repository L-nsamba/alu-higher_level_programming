#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2]; // first argument → API URL

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const todos = JSON.parse(body);
  const completedCount = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (completedCount[todo.userId]) {
        completedCount[todo.userId]++;
      } else {
        completedCount[todo.userId] = 1;
      }
    }
  });

  console.log(completedCount);
});
