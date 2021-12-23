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
    document.getElementById("kount_cutsheet").value=1;
    w.value="";
    h.value="";
    toaster("Cutsheet object dropped !","red darken-3 white-text");
}

function cutsheet_submit()
{
    var w = document.getElementById("input_sheet_width");
    var h = document.getElementById("input_sheet_height");
    var k = document.getElementById("kount_cutsheet");
    var W = w.value;    var H = h.value;
    console.log("W:"+W,"H:"+H);
    if(String(W)=="" || String(H)=="")
    {
        toaster("Empty Input","red-text text-darken-3 white");
        return("");
    }
    if(Number(W)<Number(H))
    {
        [W,H]=[H,W];
    }
    const id_ = makeid(8);
    for(var i=0;i<k.value;i++)
        db[id_+String(i)]={id:id_+String(i),shape_name:"Cut-Sheet",dimensions:"w:"+W+" ; h:"+H};
    w.value="";    h.value="";k.value=1;
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
    if(Number(W)<Number(H))
    {
        [W,H]=[H,W];
    }
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
    r.value="";document.getElementById("kount_circle").value=1;
    toaster("Circle object dropped !","red darken-3 white-text");
}

function circle_submit()
{
    var r = document.getElementById("input_circle_radius");
    var k = document.getElementById("kount_circle");
    var R = r.value;
    console.log("R:"+R);
    if(String(R)=="")
    {
        toaster("Empty Input","red-text text-darken-3 white");
        return("");
    }
    r.value="";
    const id_ = makeid(8);
    for(var i=0;i<k.value;i++)
        db[id_+String(i)]={id:id_+String(i),shape_name:"Circle",dimensions:"r:"+R};
    k.value=1;
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
    r.value="";document.getElementById("kount_cone").value=1;
    toaster("Cone object dropped !","red darken-3 white-text");
}

function sector_cancel()
{
    var r = document.getElementById("input_sector_radius");
    var a = document.getElementById("input_sector_angle");
    a.value="";
    r.value="";document.getElementById("kount_sector").value=1;
    toaster("Sector object dropped !","red darken-3 white-text");
}

function frustum_cancel()
{
    var R = document.getElementById("input_frustum_R")
    var r = document.getElementById("input_frustum_r");
    var h = document.getElementById("input_frustum_height");
    h.value="";R.value="";
    r.value="";document.getElementById("kount_frustum").value=1;
    toaster("Frustum object dropped !","red darken-3 white-text");
}

function segment_cancel()
{
    var R = document.getElementById("input_segment_R")
    var r = document.getElementById("input_segment_r");
    var h = document.getElementById("input_segment_angle");
    h.value="";R.value="";
    r.value="";document.getElementById("kount_segment").value=1;
    toaster("Segment object dropped !","red darken-3 white-text");
}

function frustum_submit()
{
    var h = document.getElementById("input_frustum_height");
    var r = document.getElementById("input_frustum_r");
    var R = document.getElementById("input_frustum_R");
    var k = document.getElementById("kount_frustum");
    var h_ = h.value;  var r_ = r.value; var R_ = R.value;
    if(String(h_)=="" || String(r_)=="" || String(R_)=="")
    {
        toaster("Empty Input","red-text text-darken-3 white");
        return("");
    }
    if(Number(r_)>=Number(R_))
    {
        toaster("Frustum<br>r >= R error","red-text text-darken-3 white");
        console.log(r_,">",R_,r_>R_);
        return("");
    }
    console.log("H:"+h_,"r:"+r_,"R"+R_);
    h.value="";    r.value=""; R.value="";
    const id_ = makeid(8);
    for(var i=0;i<k.value;i++)
        db[id_+String(i)]={id:id_+String(i),shape_name:"Frustum",dimensions:"h:"+h_+" ; R:"+R_+" ; r:"+r_};
    k.value=1;
    var instance = M.Modal.getInstance(document.getElementById("modal_frustum"));    instance.close()
    toaster("Frustum object added to stack !","yellow-text text-darken-2");
    table_refresh();
}

function segment_submit()
{
    var h = document.getElementById("input_segment_angle");
    var r = document.getElementById("input_segment_r");
    var R = document.getElementById("input_segment_R");
    var k = document.getElementById("kount_segment");
    var h_ = h.value;  var r_ = r.value; var R_ = R.value;
    if(String(h_)=="" || String(r_)=="" || String(R_)=="")
    {
        toaster("Empty Input","red-text text-darken-3 white");
        return("");
    }
    if(Number(r_)>=Number(R_))
    {
        toaster("Segment<br>r >= R error","red-text text-darken-3 white");
        console.log(r_,">",R_,r_>R_);
        return("");
    }
    if(Number(h_)<0 || Number(h_)>360)
    {
        toaster("Invalid Segment Dimensions<br>"+String(h_)+" degrees","red-text text-darken-3 white");
        return("");
    }
    console.log("θ:"+h_,"r:"+r_,"R"+R_);
    h.value="";    r.value=""; R.value="";
    const id_ = makeid(8);
    for(var i=0;i<k.value;i++)
        db[id_+String(i)]={id:id_+String(i),shape_name:"Segment",dimensions:"R:"+R_+" ; r:"+r_+" ; t:"+h_ };
    k.value=1;
    var instance = M.Modal.getInstance(document.getElementById("modal_segment"));    instance.close()
    toaster("Segment object added to stack !","yellow-text text-darken-2");
    table_refresh();
}

function cone_submit()
{
    var h = document.getElementById("input_cone_height");
    var r = document.getElementById("input_cone_radius");
    var k = document.getElementById("kount_cone");
    var H = h.value;  var R = r.value;
    var l = Math.round(Math.sqrt(R*R + H*H)*100)/100;
    var theta = 360*R/l;
    if(String(R)=="" || String(H)=="")
    {
        toaster("Empty Input","red-text text-darken-3 white");
        return("");
    }
    if(Number(theta)<0 || Number(theta)>360)
    {
        toaster("Invalid Cone Dimensions<br>"+String(theta)+" degrees","red-text text-darken-3 white");
        return("");
    }
    console.log("H:"+H,"R:"+R);
    h.value="";    r.value="";
    const id_ = makeid(8);
    for(var i=0;i<k.value;i++)
        db[id_+String(i)]={id:id_+String(i),shape_name:"Cone",dimensions:"h:"+H+" ; r:"+R};
    k.value=1;
    var instance = M.Modal.getInstance(document.getElementById("modal_cone"));    instance.close()
    toaster("Cone object added to stack !","yellow-text text-darken-2");
    table_refresh();
}

function sector_submit()
{
    var r = document.getElementById("input_sector_radius");
    var a = document.getElementById("input_sector_angle");
    var k = document.getElementById("kount_sector");
    var A = a.value;  var R = r.value;
    if(String(R)=="" || String(A)=="")
    {
        toaster("Empty Input","red-text text-darken-3 white");
        return("");
    }
    if(Number(A)<0 || Number(A)>360)
    {
        toaster("Invalid Sector Dimensions<br>"+String(A)+" degrees","red-text text-darken-3 white");
        return("");
    }
    console.log("R:"+R,"θ:"+A);
    r.value="";    a.value="";
    const id_ = makeid(8);
    for(var i=0;i<k.value;i++)
        db[id_+String(i)]={id:id_+String(i),shape_name:"Sector",dimensions:"r:"+R+" ; theta:"+A};
    k.value=1;
    var instance = M.Modal.getInstance(document.getElementById("modal_sector"));    instance.close()
    toaster("Sector object added to stack !","yellow-text text-darken-2");
    table_refresh();
}

//         Publisher

function process_cancel()
{
    toaster("Process Dropped","red darken-3 white-text",false);
}

function publish()
{
    if(Object.keys(db).length === 0)
        toaster("Empty Inventory !","white-text red darken-3",false);
    else
        if(canvasExists==false)
            toaster("No CANVAS","white-text red darken-3",false);
        else
        {
            db["__data__"]={"t":"3","a":"4","cc":"75"}
            socket.emit("process!",db);
            toaster("Process Initiated","green-text white text-darken-3",false);
            var btn_li=document.getElementsByClassName("btn")
            for(var i = 0; i < btn_li.length; i++)
                btn_li[i].disabled=true;
            btn_li=document.getElementsByClassName("btn-large")
            for(var i = 0; i < btn_li.length; i++)
                btn_li[i].disabled=true;
            document.getElementById("info_div").style.display="block";
            document.getElementById("shopping_list").style.display="none";
        }
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

//               CUSTOM OBJECTS
function custom_cancel()
{
    var k = document.getElementById("kount_custom");
    var f = document.getElementById("myfileinput");
    document.getElementById("input_name").value="";
    k.value=1;    f.type="password";    f.type="file";
    toaster("Custom object dropped !","red darken-3 white-text");
}

function custom_submit(filedata)
{
    var n = document.getElementById("input_name");
    var k = document.getElementById("kount_custom");
    if(n.value.trim()=="")
    {
        toaster("No Shape Name Specified","white-text red darken-3",false);
        return("");
    } 
    //console.log(filedata);
    const id_ = makeid(8);
    for(var i=0;i<k.value;i++)
        db[id_+String(i)]={id:id_+String(i),shape_name:"CUSTOM-"+String(n.value.trim()),dimensions:"File Upload Successful",filedata:filedata};
    k.value=1;n.value = "";
    var instance = M.Modal.getInstance(document.getElementById("modal_custom"));    instance.close()
    toaster("Custom object added to stack !","yellow-text text-darken-2");
    table_refresh();
    var k = document.getElementById("kount_custom");
    var f = document.getElementById("myfileinput");
    document.getElementById("input_name").value="";
    k.value=1;    f.type="password";    f.type="file";
    console.log(filedata);
}

var button = document.getElementById("send-file-button");
var fileInput = document.getElementById("myfileinput");
var output = document.getElementById("output");

button.onclick = function () {
  var files = fileInput.files;
  if(files.length==0)
    {
        toaster("No File Uploaded","white-text red darken-3",false);
        return("")   ;
    }
  var reader = new FileReader();
  reader.onload = function () {
    custom_submit(reader.result);
  };
  if(files[0]) {
    reader.readAsText(files[0]);
  }
};