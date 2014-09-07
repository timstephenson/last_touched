#!/usr/bin/env node
touch = require('./touch');

touch.loadFileStats( process.argv.slice(2) );
touch.printLastTouched();