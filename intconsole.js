#!/usr/bin/env node

const { exec } = require('child_process');

exec('python3 intconsoleV4.py', (error, stdout, stderr) => {
  if (error) {
    console.error(`Hata: ${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`Stderr: ${stderr}`);
    return;
  }
  console.log(`Stdout: ${stdout}`);
});