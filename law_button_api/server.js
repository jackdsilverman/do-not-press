require('dotenv').config();
const express = require('express')
const https = require('https');
const fs = require('fs');

const app = express()
const port = 3000

const options = {
    key: fs.readFileSync(process.env.SSL_KEY_PATH),
    cert: fs.readFileSync(process.env.SSL_CERT_PATH)
  };

var counter = 0;

app.post('/law-button', (req, res) => {
    counter++
    res.send(`Number of times button has been pressed: ${counter}`)
})

app.post('/reset-button', (req, res) => {
    counter = 0
    res.send(`Counter has been reset to ${counter}`)
})

https.createServer(options, app).listen(port, () => {
    console.log(`Example app listening securely on https://localhost:${port}`);
})