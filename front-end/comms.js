var socket = io();

socket.on("Process Confirmation",(status)=>{
    console.log(status);
});

socket.on("notification",(data)=>{
    console.log("Notif : ",data);
    toaster(data,"white-text green darken-2 ");
});

socket.on("logs",(data)=>{
    console.log("logs : ",data);
    document.getElementById("log_div").innerText=data;
});

socket.on("Free Space",(status)=>{
    if(status=="Success")
        toaster("Cache Cleared","green-text white text-darken-2");
    else
        toaster("Cache Clear Failed","white-text red darken-2");
});