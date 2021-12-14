var socket = io();

socket.on("Process Confirmation",(status)=>{
    console.log(status);
})