#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2]; // first argument → API URL

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach(film => {
    if (film.characters.some(charUrl => charUrl.endsWith('/18/'))) {
      count++;
    }
  });

  console.log(count);
});
