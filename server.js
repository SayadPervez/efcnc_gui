const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
const fs = require('fs')

var data = fs.readFileSync('./pyprogs/log.txt', 'utf8');

app.use(express.static('./front-end'));

function replaceAll(str, find, replace) {
  return str.replace(new RegExp(find, 'g'), replace);
}

setInterval(function(){ 
  d = fs.readFile('./pyprogs/log.txt', 'utf8',()=>{
    io.emit("logs",d);
  })
},1000)

io.on('connection', (socket) => {
    //testing
    socket.on('Hi', (msg) => {
      console.log('message: ' + JSON.stringify(msg));
      io.to(socket.id).emit("Hi","Hi");
    });
    //process reception
    socket.on("process!",(db)=>{
      fs.writeFile('./pyprogs/log.txt', '',()=>{});
        x=( 
          replaceAll(
          replaceAll(
          replaceAll(replaceAll(JSON.stringify(db),'\n',''),"\r",""),
          '\"','"'
          ),'"','^')
          );
        console.log(cmdline(`cd ./pyprogs/ && python main.py "${x}"`));
        io.to(socket.id).emit("Process Confirmation","Success");
    });
    socket.on("_mod.js",(data)=>{
      //console.log(data);
      io.to(socket.id).emit("die","from server");
      io.emit("notification",data);
    });
    socket.on("Free Space",(x)=>{
      console.log("Clear Request");
      out=cmdline("cd ./pyprogs/ && python free_space.py");
      if(out=="Success\r\n")
        io.to(socket.id).emit("Free Space","Success");
      else
        io.to(socket.id).emit("Free Space","Failure");
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