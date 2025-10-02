#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2]; // first argument → API URL

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body).results;
  let count = 0;

  data.forEach(film => {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  });

  console.log(count);
});
