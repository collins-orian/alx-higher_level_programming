#!/usr/bin/node

const urlLink = process.argv[2];
const request = require('request');

request(urlLink, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
