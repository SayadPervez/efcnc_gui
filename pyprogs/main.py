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
            print("canvas created")
        elif(name_=="Cut-Sheet"):
            w,h = list(map(float,dim_))
            CutSheet(w,h,0,id_)
            pushNotification("Cut-Sheet Created")
            print("cutsheet created")

if len(sys.argv)>1:
    print("server started")
    RUN((sys.argv[1]).replace("^",'"'))
