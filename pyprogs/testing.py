from shapeManager import *
from visualization import *
import algorithm1,algorithm2,algorithm4,algorithm3,algorithm5,algorithm6,algorithme
from svgBuilder import svgPlacer,svgRotate

freeSpace()
thickness = [1]
canvas__ = Canvas(250,450)
objList = [
    Flange(":tbee_95_6","flange"),Circle(7,"circ")   ,
    CutSheet(30,10,0,"rect"),CutSheet(25,25,0,"rect22"),CutSheet(3,3,0,"rect2"),
    Cone(20,7,0,"cnt1"),Sector(20,60,0,"sec_t1")     ,
    Frustum(20,5,20,0,"frust"),Segment(20,10,60,0,"segs")
    ]

for obj in objList:
    obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]))

out,shapes,up = binaryFilter(algorithme.run(canvas__,objList,log_=True,constCompute=3,returnOrder=True))
arr2png(out).show()
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
print("end")
for _ in up:
    print(_,end="\n\n")
