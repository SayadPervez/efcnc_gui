db = {};
var Kount = 0;
var canvasExists = false;

//              Delete

function del_cancel()
{
    toaster("Deletion Cancelled !","green darken-3 white",false);
}

function del_submit()
{
    var instance = M.Modal.getInstance(document.getElementById("modal_delete_row"));    instance.close()
    
    var temp = document.getElementById("deletion_id").innerText;
    if(db[temp]["shape_name"]=="Canvas")
    {
        canvasExists=false;
        toaster("Canvas Deleted","red darken-2 white-text",false);
    }
    else{
        toaster("Object Deleted","red darken-2 white-text",false);
    }
    delete db[temp];table_refresh();
}

//              Cutsheet

function cutsheet_cancel()
{
    var w = document.getElementById("input_sheet_width");
    var h = document.getElementById("input_sheet_height");
    w.value="";
    h.value="";
    toaster("Cutsheet object dropped !","red darken-3 white-text");
}

function cutsheet_submit()
{
    var w = document.getElementById("input_sheet_width");
    var h = document.getElementById("input_sheet_height");
    var W = w.value;    var H = h.value;
    console.log("W:"+W,"H:"+H);
    if(String(W)=="" || String(H)=="")
    {
        toaster("Empty Input","red-text text-darken-3 white");
        return("");
    }
    w.value="";    h.value="";
    const id_ = makeid(8);
    db[id_]={id:id_,shape_name:"Cut-Sheet",dimensions:"w:"+W+" ; h:"+H};
    var instance = M.Modal.getInstance(document.getElementById("modal_cutsheet"));    instance.close()
    toaster("Cutsheet object added to stack !","yellow-text text-darken-2");
    table_refresh();
}

//             Canvas

function canvas_cancel()
{
    var w = document.getElementById("input_canvas_width");
    var h = document.getElementById("input_canvas_height");
    w.value="";
    h.value="";
    toaster("Canvas dropped !","red darken-3 white-text");
}

function canvas_submit()
{
    var w = document.getElementById("input_canvas_width");
    var h = document.getElementById("input_canvas_height");
    var W = w.value;    var H = h.value;
    console.log("W:"+W,"H:"+H);
    if(String(W)=="" || String(H)=="")
    {
        toaster("Empty Input","red-text text-darken-3 white");
        return("");
    }
    if(canvasExists==true)
    {
        toaster("Canvas Already Exists","red-text text-darken-3 white");
        return("");
    }
    w.value="";    h.value="";
    const id_ = makeid(8);
    db[id_]={id:id_,shape_name:"Canvas",dimensions:"w:"+W+" ; h:"+H};
    var instance = M.Modal.getInstance(document.getElementById("modal_canvas"));    instance.close()
    toaster("Canvas Created !","yellow-text text-darken-2");
    table_refresh();
    canvasExists=true;
}

//             Circle

function circle_cancel()
{
    var r = document.getElementById("input_circle_radius");
    r.value="";
    toaster("Circle object dropped !","red darken-3 white-text");
}

function circle_submit()
{
    var r = document.getElementById("input_circle_radius");
    var R = r.value;
    console.log("R:"+R);
    if(String(R)=="")
    {
        toaster("Empty Input","red-text text-darken-3 white");
        return("");
    }
    r.value=""
    const id_ = makeid(8);
    db[id_]={id:id_,shape_name:"Circle",dimensions:"r:"+R};
    var instance = M.Modal.getInstance(document.getElementById("modal_circle"));    instance.close()
    toaster("Circle object added to stack !","yellow-text text-darken-2");
    table_refresh();
}

//         Cone

function cone_cancel()
{
    var h = document.getElementById("input_cone_height");
    var r = document.getElementById("input_cone_radius");
    h.value="";
    r.value="";
    toaster("Cone object dropped !","red darken-3 white-text");
}

function cone_submit()
{
    var h = document.getElementById("input_cone_height");
    var r = document.getElementById("input_cone_radius");
    var H = h.value;  var R = r.value;
    var l = Math.round(Math.sqrt(R*R + H*H)*100)/100;
    var theta = 360*R/l;
    if(String(R)=="" || String(H)=="")
    {
        toaster("Empty Input","red-text text-darken-3 white");
        return("");
    }
    if(theta<0 || theta>360)
    {
        toaster("Invalid Cone Dimensions<br>"+String(theta),"red-text text-darken-3 white");
        return("");
    }
    console.log("H:"+H,"R:"+R);
    h.value="";    r.value="";
    const id_ = makeid(8);
    db[id_]={id:id_,shape_name:"Cone",dimensions:"h:"+H+" ; r:"+R};
    var instance = M.Modal.getInstance(document.getElementById("modal_cone"));    instance.close()
    toaster("Cone object added to stack !","yellow-text text-darken-2");
    table_refresh();
}

//         Publisher

function publish()
{
    if(Object.keys(db).length === 0)
        toaster("Empty Inventory !","white-text red darken-3",false);
    else
        socket.emit("process!",db);
}

function clean()
{
    socket.emit("Free Space","Please");
}

function lock()
{
    var x=document.getElementById("lock_span");
    if(x.innerText=="lock")
    {
        x.innerText="lock_open";
        x.style.color = "red";
        document.getElementById("canvas_width").disabled=false;
        document.getElementById("canvas_height").disabled=false;
    }
    else
    {
        x.innerText="lock";
        x.style.color = "green";
        document.getElementById("canvas_width").disabled=true;
        document.getElementById("canvas_height").disabled=true;
    }
}