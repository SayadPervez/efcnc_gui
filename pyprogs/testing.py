from shapeManager import *
from visualization import *
import algorithm1,algorithm2
from svgBuilder import svgPlacer

thickness = [3]
canvas__ = Canvas(1000,500)
objList = [Circle(70,"circle_"),CutSheet(200,20,0,"cutshett")]

for obj in objList:
        if(thickness[0]<6):
            obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]//4)+1)
        else:
            obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]//2+1)*2)

out,shapes = binaryFilter(algorithm2.run(canvas__,objList,log_=True,constCompute=1000,returnOrder=True))

xl,yl=[],[]
cx,cy = canvas__.length,canvas__.height
for shape in shapes:
    print(shape.myShape,shape.low_res_pos)
    px , py , _ = shape.low_res_pos
    px,py = math.floor(px/100*cx),math.floor(py/100*cy)
    xl.append(px)
    yl.append(py)
svgPlacer(canvas__.svgPath,[_.svgPath for _ in shapes],xl,yl,thickness[0])
arr2png(out).show()
print("end")