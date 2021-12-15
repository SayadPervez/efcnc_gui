var socket = io();

socket.on("Process Confirmation",(status)=>{
    console.log(status);
});

socket.on("Free Space",(status)=>{
    if(status=="Success")
        toaster("Cache Cleared","green-text white text-darken-2");
    else
        toaster("Cache Clear Failed","white-text red darken-2");
});