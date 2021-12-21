from shapeManager import *
from visualization import *
import algorithm1,algorithm2,algorithm4,algorithm3
from svgBuilder import svgPlacer,svgRotate

freeSpace()
thickness = [3]
canvas__ = Canvas(200,200)
objList = [
    Cone(50,30,0,"Conehere"),
    Cone(50,30,0,"Conehere1"),
    Cone(50,30,0,"Conehere2"),
    Cone(20,10,0,"Conehere3"),
    Cone(20,10,0,"Conehere4"),
    Cone(20,10,0,"Conehere5"),
    Cone(20,10,0,"Conehere6"),
    Cone(20,10,0,"Conehere7"),
    Cone(20,10,0,"Conehere6"),
    Cone(20,10,0,"Conehere7")
    ]

for obj in objList:
        if(thickness[0]<6):
            obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]//4)+1)
        else:
            obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]//2+1)*2)

out,shapes = binaryFilter(algorithm3.run(canvas__,objList,log_=True,constCompute=50,returnOrder=True))
arr2png(out).show()
# for A3
if(True):
    for shape in shapes:
        svgRotate(shape.svgPath,shape.angle)
xl,yl=[],[]
cx,cy = canvas__.length,canvas__.height
for shape in shapes:
    print(shape.myShape,shape.low_res_pos)
    px , py , _ = shape.low_res_pos
    px,py = math.floor(px/100*cx),math.floor(py/100*cy)
    xl.append(px)
    yl.append(py)
svgPlacer(canvas__.svgPath,[_.svgPath for _ in shapes],xl,yl,thickness[0])
print("end")