from shapeManager import *
from visualization import *
import algorithm1,algorithm2,algorithm4,algorithm3
from svgBuilder import svgPlacer,svgRotate

freeSpace()
thickness = [3]
canvas__ = Canvas(100,100)
objList = [
    CutSheet(80,80,0,"cutsheet"),
    CutSheet(10,10,0,"cutsheet1"),
    Circle(12,"circ")
    ]

for obj in objList:
        if(thickness[0]<6):
            obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]//4)+1)
        else:
            obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]//2+1)*2)

out,shapes,up = binaryFilter(algorithm3.run(canvas__,objList,log_=True,constCompute=75,returnOrder=True))
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