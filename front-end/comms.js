var socket = io();

socket.on("ppp",(status)=>{
    if(status=="Success")
    {
    toaster("Task Completion "+String(status),"white-text green darken-2 ");
    document.getElementById("info_butt").innerHTML = `<strong>Process Completed ...</strong>`;
    document.getElementById("info_butt").classList.remove("red");
    document.getElementById("info_butt").classList.add("green");
    }
    else{
        toaster("Task Failed ","white-text red darken-3");
        document.getElementById("info_butt").innerHTML = `<strong>Process Failed ...</strong>`;
    }
});

socket.on("notification",(data)=>{
    console.log("Notif : ",data);
    toaster(data,"white-text green darken-2 ");
});

socket.on("exception2front",(data)=>{
    console.log("Exception : ",data);
    toaster(data,"white-text red darken-3",false);
});

socket.on("Free Space",(status)=>{
    if(status=="Success")
        toaster("Cache Cleared","green-text white text-darken-2");
    else
        toaster("Cache Clear Failed","white-text red darken-2");
});