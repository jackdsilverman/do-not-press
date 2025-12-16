require('dotenv').config();
const express = require('express')
const serverless = require('serverless-http');

const app = express()

var counter = 0;

app.post('/button', (req, res) => {
    counter++
    res.send(`Number of times button has been pressed: ${counter}`)
})

app.post('/reset', (req, res) => {
    counter = 0
    res.send(`Counter has been reset to ${counter}`)
})

app.get('/count', (req, res) => {
    res.send(`Number of times button has been pressed: ${counter}`)
})

module.exports.handler = serverless(app);