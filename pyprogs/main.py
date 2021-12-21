from svgBuilder import svgPlacer,svgRotate
from shapeManager import *
from functions import *
import algorithm1,algorithm2,algorithm3,algorithm4
from visualization import *
import sys
from json import loads as jsonparser
import math
from winsound import Beep as beep

objList=[]
thickness=[]
alg = []
canvas__=None

def RUN(jsonString):
    db = (jsonparser(jsonString))
    for objectkey in db:
        if("__data__" == objectkey):
            thickness .append( float((db["__data__"])["t"]) )
            alg .append( int((db["__data__"])["a"]) )
            beep(4000,700)
            continue
        obj = db[objectkey]
        id_ = objectkey
        name_ = obj["shape_name"]
        dim_ = obj["dimensions"]
        for _ in dim_:
            if(_ in ([chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]+[":"])):
                dim_ = dim_.replace(_,"")
        dim_ = dim_.split(";")
        print(f"shape_name : {name_} ; id : {id_} ; dimensions : {dim_}")
        
        if(name_=="Canvas"):
            w,h = list(map(float,dim_))
            canvas__=Canvas(w,h)
            pushNotification("Canvas Created")
        elif(name_=="Cut-Sheet"):
            w,h = list(map(float,dim_))
            objList.append(CutSheet(w,h,0,id_))
            pushNotification("Cut-Sheet Created")
        elif(name_=="Circle"):
            r = float(dim_[0])
            objList.append(Circle(r,id_))
            pushNotification("Circle Created")
        elif(name_=="Cone"):
            h,r = list(map(float,dim_))
            objList.append(Cone(h,r,0,id_))
            pushNotification("Cone Created")
        elif(name_=="Sector"):
            r,t = list(map(float,dim_))
            objList.append(Sector(r,t,0,id_))
            pushNotification("Sector Created")
        elif(name_=="Frustum"):
            h,R,r = list(map(float,dim_))
            objList.append(Frustum(R,r,h,0,id_))
            pushNotification("Frustum Created")
        elif(name_=="Segment"):
            R,r,t = list(map(float,dim_))
            objList.append(Segment(R,r,t,0,id_))
            pushNotification("Segment Created")
        elif(name_.startswith("CUSTOM-")):
            fd = obj["filedata"]
            objList.append(Custom(fd,id_))
            pushNotification("Custom Object Created")
        pushNotification("Process Completed")

    print("algorithm:",alg[0])
    print("thickness:",thickness[0])
    for obj in objList:
        if(thickness[0]<6):
            obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]//4)+1)
        else:
            obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]//2+1)*2)
            print("else thickness executed")
    print("Starting low level algorithm")
    if(alg[0] == 1):
        out,shapes = binaryFilter(algorithm1.run(canvas__,objList,log_=True,constCompute=1000,returnOrder=True))
    elif(alg[0] == 2):
        out,shapes = binaryFilter(algorithm2.run(canvas__,objList,log_=True,constCompute=80,returnOrder=True))
    elif(alg[0] == 3):
        out,shapes = binaryFilter(algorithm3.run(canvas__,objList,log_=True,constCompute=1000,returnOrder=True))
    elif(alg[0] == 4):
        out,shapes = binaryFilter(algorithm4.run(canvas__,objList,log_=True,constCompute=1000,returnOrder=True))
    else:
        raise Exception("Invalid Algorithm")
    if(alg[0] == 3):
        print("Starting svg rotation")
        for shape in shapes:
            svgRotate(shape.svgPath,shape.angle)
    print("Starting svg positioning")
    xl,yl=[],[]
    cx,cy = canvas__.length,canvas__.height
    for shape in shapes:
        px , py , _ = shape.low_res_pos
        px,py = math.floor(px/100*cx),math.floor(py/100*cy)
        xl.append(px)
        yl.append(py)
    svgPlacer(canvas__.svgPath,[_.svgPath for _ in shapes],xl,yl,thickness[0])
    #arr2png(out).show()
    print("end")

if len(sys.argv)>1:
    print("server started")
    freeSpace()
    RUN((sys.argv[1]).replace("^",'"'))
