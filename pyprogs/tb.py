from cProfile import label
from shapeManager import *
from visualization import *
import algorithm1,algorithm2,algorithm4,algorithm3,algorithm5,algorithm6
from svgBuilder import svgPlacer,svgRotate
import time

addr = "./IMG/tb_images/"

timeList = []
unplacedList = []

s_ = time.time()

freeSpace()
thickness = [1]
cc = 3
canvas__ = Canvas(180,180)
objList = [
    Flange(":tbee_95_6","flange"),Circle(7,"circ")   ,
    CutSheet(30,10,0,"rect"),CutSheet(25,25,0,"rect22"),CutSheet(3,3,0,"rect2"),
    Cone(20,7,0,"cnt1"),Sector(20,60,0,"sec_t1")     ,
    Frustum(20,5,20,0,"frust"),Segment(20,10,60,0,"segs")
    ]

for obj in objList:
    obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]))

s__ = time.time()

objectCreationTime = s__ - s_
print(f"objectCreationTime : {objectCreationTime} secs")

for alg in range(1,7):
    print(f"Starting alg {alg}")
    s0 = time.time()
    if(alg == 1):
        out,shapes,up = binaryFilter(algorithm1.run(canvas__,objList,log_=True,constCompute=cc,returnOrder=True))
    elif(alg == 2):
        out,shapes,up = binaryFilter(algorithm2.run(canvas__,objList,log_=True,constCompute=cc,returnOrder=True))
    elif(alg == 3):
        out,shapes,up = binaryFilter(algorithm3.run(canvas__,objList,log_=True,constCompute=cc,returnOrder=True))
    elif(alg == 4):
        out,shapes,up = binaryFilter(algorithm4.run(canvas__,objList,log_=True,constCompute=cc,returnOrder=True))
    elif(alg == 5):
        out,shapes,up = binaryFilter(algorithm5.run(canvas__,objList,log_=True,constCompute=cc,returnOrder=True))
    elif(alg == 6):
        out,shapes,up = binaryFilter(algorithm6.run(canvas__,objList,log_=True,constCompute=cc,returnOrder=True))
    else:
        pushError("Invalid Algorithm")
        raise Exception("Invalid Algorithm")
    #arr2png(out).show()
    # for A3
    if(True):
        for shape in shapes:
            if(shape.placed==False):
                continue
            if(shape.angle==0 or shape.angle%360==0):
                continue
            svgRotate(shape.svgPath,shape.angle)
    xl,yl=[],[]
    cx,cy = canvas__.length,canvas__.height
    for shape in shapes:
        if shape.placed==False:
            continue
        print(shape.myShape,shape.low_res_pos)
        px , py , _ = shape.low_res_pos
        px,py = math.floor(px/100*cx),math.floor(py/100*cy)
        xl.append(px)
        yl.append(py)
    svgPlacer(canvas__.svgPath,[_.svgPath for _ in shapes],xl,yl,thickness[0])
    if(up!=[]):
        unplacedList.append((True,len(up),up))
    else:
        unplacedList.append((False,len(up)))
    timeList.append(time.time()-s0)
    print(f"End of alg {alg}")
    #arr2png(out).show()
    arr2png(out).save(f"{addr}algorithm_{alg}.png")
    abc = free_surface_all(out,40)
    arr2png(abc).show()
    pieChart(free_surface_area(abc),f"Algorithm {alg}")
    input("Hit enter to continue ...")
    for _ in up:
        print(_,end="\n\n")

print("Results : ")
print(f"Object Creation Time : {objectCreationTime} secs")
for a in range(0,6):
    print(f"Algorithm {a+1} : {timeList[a]} secs : {f'{unplacedList[a][1]} Unplaced : {unplacedList[a][2]}' if (unplacedList[a][0]) else 'All Placed !!'}")

import numpy as np
import matplotlib.pyplot as plt
x = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
y = [objectCreationTime+_ for _ in timeList]
z = ["red" if unplacedList[_][0] else "green" for _ in range(0,6)]
plt.title="Algorithm Time Complexity"
plt.xlabel("Time")
plt.ylabel("Algorithm")
plt.legend()
plt.barh(x,y,color=z)
plt.show()
