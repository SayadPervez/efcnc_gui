from shapeManager import *
from visualization import *
import algorithm1,algorithm2,algorithm4
from svgBuilder import svgPlacer

thickness = [3]
canvas__ = Canvas(400,400)
objList = [CutSheet(395,90,0,"csgo"),CutSheet(30,300,0,"cs2"),Circle(30,"circle_2_12_"),Circle(50,"circle_2_234234_"),Circle(40,"circle_2_q3weqwer_"),Circle(30,"circle_2__"),Circle(40,"circle_1__"),Circle(90,"circle_2_3_"),Circle(40,"circle1_2_1_"),Circle(30,"circlesrdfe1_2_1_")]

for obj in objList:
        if(thickness[0]<6):
            obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]//4)+1)
        else:
            obj.shapeMatrix = outline_with_shape(obj,int(thickness[0]//2+1)*2)

out,shapes = binaryFilter(algorithm4.run(canvas__,objList,log_=True,constCompute=50,returnOrder=True))
arr2png(out).show()
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