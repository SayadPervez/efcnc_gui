from functions import *
from shapes import *
import algorithm1,algorithm2,algorithm3,algorithm4
import constants as cont
from visualization import *

print("\na1-S starting:")
canvas = Canvas(200,100)
shapes = [ 
            Square(20) ,
            Rectangle(35,25) , 
            Circle(7) ,
            Cone(17,20) ,
            Cone(12,4)
        ]
for shape in shapes:
    shape.shapeMatrix = outline_with_shape(shape,3)

c = canvas
li = shapes
print("Starting algorithm1")
out = algorithm1.run(c,li,log_=True,constCompute=50)
arr2png(out).show()
input("Press ENTER to continue ...")
out=binaryFilter(out)
out = free_surface_all(out,70)
arr2png(out).show()
input("Press ENTER to continue ...")
pieChart(free_surface_area(out))


input("Start next algorithm ?")

print("\na2-S starting:")
canvas = Canvas(108,72)
shapes    = [ 
            Square(20) ,
            Rectangle(10,25) , 
            Circle(7) ,
            Cone(17,20) ,
            Cone(12,4)
        ]
for shape in shapes:
    shape.shapeMatrix = outline_with_shape(shape,3)
c = canvas
li = shapes
print("Starting algorithm2")
out = algorithm2.run(c,li,log_=True,constCompute=50)
arr2png(out).show()
input("Press ENTER to continue ...")
out=binaryFilter(out)
out = free_surface_all(out,70)
arr2png(out).show()
input("Press ENTER to continue ...")
pieChart(free_surface_area(out))


input("Start next algorithm ?")

canvas = Canvas(108,108)
shapes    = [ 
            Square(20) ,
            Rectangle(10,25) , 
            Circle(7) ,
            Cone(17,20),
            Cone(12,4),
            Cone(12,4),
            Cone(12,4),
            Cone(12,4)
        ]
for shape in shapes:
    shape.shapeMatrix = outline_with_shape(shape,3)
c = canvas
li = shapes
print("Starting algorithm3")
out = algorithm3.run(c,li,log_=True,constCompute=75)
arr2png(out).show()
input("Press ENTER to continue ...")
out=binaryFilter(out)
out = free_surface_all(out,70)
arr2png(out).show()
input("Press ENTER to continue ...")
pieChart(free_surface_area(out))


print("\na4-S starting:")
canvas = Canvas(108,72)
shapes    = [ 
            Square(20) ,
            Rectangle(10,25) , 
            Circle(7) ,
            Cone(17,20) ,
            Cone(12,4)
        ]
for shape in shapes:
    shape.shapeMatrix = outline_with_shape(shape,3)
c = canvas
li = shapes
print("Starting algorithm4")
out = algorithm4.run(c,li,log_=True,constCompute=75)
arr2png(out).show()
input("Press ENTER to continue ...")
out=binaryFilter(out)
out = free_surface_all(out,60)
arr2png(out).show()
input("Press ENTER to continue ...")
pieChart(free_surface_area(out))

