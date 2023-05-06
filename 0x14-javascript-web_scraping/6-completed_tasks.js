#!/usr/bin/node

const urlLink = process.argv[2];
const request = require('request');

request(urlLink, function (error, resp, body) {
  if (error) {
    console.log(error);
  } else if (resp.statusCode === 200) {
    const dic = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      if (tasks[i].completed) {
        if (dic[tasks[i].userId] === undefined) {
          dic[tasks[i].userId] = 1;
        } else {
          dic[tasks[i].userId]++;
        }
      }
    }
    console.log(dic);
  } else {
    console.log('erroror code: ' + resp.statusCode);
  }
});
