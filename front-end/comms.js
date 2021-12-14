var socket = io();
socket.emit("Hi","Hi");

socket.on("Hi",(rly)=>{
    console.log(rly);
})