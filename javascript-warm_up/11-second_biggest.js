#!/usr/bin/node
 const args = process.argv.slice(2);
 if (args.length === 0) {
  console.log('0');
} else if (args.length === 1) {
  console.log('0');
}
 if (args.length > 1) {
  const sortedArgs = args.sort();
  const secondLastArg = sortedArgs[sortedArgs.length - 2];
  console.log(secondLastArg);
}
