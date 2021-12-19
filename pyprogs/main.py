from shapeManager import *
from functions import *
import algorithm1,algorithm2,algorithm3,algorithm4
from visualization import *
import sys
from json import loads as jsonparser

def RUN(jsonString):
    db = (jsonparser(jsonString))
    for objectkey in db:
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
            Canvas(w,h)
            pushNotification("Canvas Created")
        elif(name_=="Cut-Sheet"):
            w,h = list(map(float,dim_))
            CutSheet(w,h,0,id_)
            pushNotification("Cut-Sheet Created")
        elif(name_=="Circle"):
            r = float(dim_[0])
            Circle(r,id_)
            pushNotification("Circle Created")
        elif(name_=="Cone"):
            h,r = list(map(float,dim_))
            Cone(h,r,0,id_)
            pushNotification("Cone Created")
        elif(name_=="Sector"):
            r,t = list(map(float,dim_))
            Sector(r,t,0,id_)
            pushNotification("Sector Created")
        elif(name_=="Frustum"):
            h,R,r = list(map(float,dim_))
            Frustum(R,r,h,0,id_)
            pushNotification("Frustum Created")
        elif(name_=="Segment"):
            R,r,t = list(map(float,dim_))
            Segment(R,r,t,0,id_)
            pushNotification("Segment Created")
        elif(name_.startswith("CUSTOM-")):
            fd = obj["filedata"]
            Custom(fd,id_)
            pushNotification("Custom Object Created")
        pushNotification("Process Completed")

if len(sys.argv)>1:
    print("server started")
    freeSpace()
    RUN((sys.argv[1]).replace("^",'"'))
