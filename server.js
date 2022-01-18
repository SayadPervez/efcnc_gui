const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const fs = require('fs');
const io = require("socket.io")(server, {
  cors: {
    origin: "*:*"
  }
});

app.use(express.static('./front-end'));

function replaceAll(str, find, replace) {
  return str.replace(new RegExp(find, 'g'), replace);
}

io.on('connection', (socket) => {
    //testing
    console.log("Connect "+String(socket.id))
    socket.on('Hi', (msg) => {
      console.log('message: ' + JSON.stringify(msg));
      io.to(socket.id).emit("Hi","Hi");
    });
    //process reception
    socket.on("process!",(db)=>{
      cmdline("cd ./pyprogs/ && python free_space.py");
      Object.keys(db).forEach(function (key) {
        if(key!="__data__")
        {
          if((db[key]["shape_name"]).startsWith("CUSTOM-"))
          {
            // writing custom shapes here
            var obj = db[key]
            for( var i=0;i<db[key]["count"];i++){
              var name = obj["id"]+String(i)+String(".svg");
              fs.writeFileSync( "./pyprogs/SVG/"+name, obj["filedata"]);
            }
            delete obj["filedata"];
          }
        }
      });
      console.log(db);
      console.log("Quitting process here")
      return("");
        x=( 
          replaceAll(
          replaceAll(
          replaceAll(replaceAll(JSON.stringify(db),'\n',''),"\r",""),
          '\"','"'
          ),'"','^')
          );
        console.log(cmdline_(`cd ./pyprogs/ && python main.py "${x}"`));
    });
    socket.on("_mod.js",(data)=>{
      io.to(socket.id).emit("die","from server");
      io.emit("notification",data);
    });
    socket.on("exception_",(data)=>{
      io.to(socket.id).emit("die_","from server");
      io.emit("exception2front",data);
    });
    socket.on("Free Space",(x)=>{
      console.log("Clear Request");
      out=cmdline("cd ./pyprogs/ && python free_space.py");
      if(out=="Success\r\n")
        io.to(socket.id).emit("Free Space","Success");
      else
        io.to(socket.id).emit("Free Space","Failure");
    });
    function cmdline_(command){
      const exec = require('child_process').exec;
      exec(`${command}`, { encoding: 'utf-8' }, (error, stdout, stderr) => {
        if (error) {
          console.error(`exec error: ${error}, ${stderr}`);
          io.to(socket.id).emit("ppp","Error");
        }else{
        console.log(stdout);
        io.to(socket.id).emit("ppp","Success");
        }
      });
      
      
    }
});

function cmdline(command){
    const execSync = require('child_process').execSync;
    const output = execSync(`${command}`, { encoding: 'utf-8' });
    return(output);
}

app.get('/download', function(req, res){
  const file = `./pyprogs/IMG/Output.zip`;
  res.download(file);
});

server.listen(3000, () => {
  console.log('listening on *:3000');
});