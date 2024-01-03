#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const task = JSON.parse(body);
    const tasksCompleted = {};
    task.forEach(task => {
      if (task.completed) {
        if (!tasksCompleted[task.userId]) {
          tasksCompleted[task.userId] = 1;
        } else {
          tasksCompleted[task.userId]++;
        }
      }
    });
    console.log(tasksCompleted);
  }
});
