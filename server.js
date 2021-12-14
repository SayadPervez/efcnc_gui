const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

app.use(express.static('./front-end'));

io.on('connection', (socket) => {
    socket.on('Hi', (msg) => {
      console.log('message: ' + JSON.stringify(msg));
      io.to(socket.id).emit("Hi","Hi");
    });
});



server.listen(3000, () => {
  console.log('listening on *:3000');
});