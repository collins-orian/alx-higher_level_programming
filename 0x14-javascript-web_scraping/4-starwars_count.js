#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let cnt = 0;
    for (const i in movies) {
      const characs = movies[i].characters;
      for (const c in characs) {
        if (characs[c].includes('18')) {
          cnt++;
        }
      }
    }
    console.log(cnt);
  } else {
    console.log('Erorr Code:' + res.statusCode);
  }
});
