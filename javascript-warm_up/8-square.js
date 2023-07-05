#!/usr/bin/node
const size = parseInt(process.argv[2]);
console.log(isNaN(size) ? "Missing size" : ("X".repeat(size) + "\n").repeat(size));
