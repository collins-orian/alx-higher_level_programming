#!/usr/bin/node

const url_link = process.argv[2];
const request = require("request");

request(url_link, function (error, response) {
	if (error) {
		console.log(error);
	} else {
		console.log("code: " + response.statusCode);
	}
});
