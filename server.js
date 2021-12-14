const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

app.use(express.static('./front-end'));

io.on('connection', (socket) => {
    //testing
    socket.on('Hi', (msg) => {
      console.log('message: ' + JSON.stringify(msg));
      io.to(socket.id).emit("Hi","Hi");
    });
    //process reception
    socket.on("process!",(db)=>{
        //console.log(JSON.stringify(db));
        console.log(db);
        io.to(socket.id).emit("Process Confirmation","Success");
    });
});

function cmdline(command){
    const execSync = require('child_process').execSync;
    const output = execSync(`${command}`, { encoding: 'utf-8' });
    return(output);
}

server.listen(3000, () => {
  console.log('listening on *:3000');
});