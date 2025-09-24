#!/usr/bin/node

const lines = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let output = '';
for (let i = 0; i < lines.length; i++) {
  output += lines[i] + '\n';
}

console.log(output.trim());
