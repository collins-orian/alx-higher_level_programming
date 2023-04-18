#!/bin/bash
# Script that shows the Content-Length from a HTTP request


# check if a URL has been provided
if [[ -z $1 ]]; then
  echo "Please provide a URL as an argument"
  exit 1
fi

# send a request to the URL using curl and store the response body size in a variable
response_size=$(curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2)

# display the size of the response body in bytes
if [[ -n $response_size ]]; then
  echo "Response size: ${response_size} bytes"
else
  echo "Unable to retrieve the size of the response body"
fi
