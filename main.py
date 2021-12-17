from shapeManager import CutSheet,Circle,Cone,Canvas
from functions import *
import algorithm1,algorithm2,algorithm3,algorithm4
from visualization import arr2png as a2p

freeSpace()

sheet=CutSheet(30,10,0,"abcdefgh1")
circle = Circle(50,"qwerty1")
cone = Cone(30,10,0,"zxcvb1")
canva=Canvas(1920,1080)
li = [sheet,circle,cone]

out = algorithm1.run(canva,li,log_=True,constCompute=100)
a2p(out).show()

for _ in li:
    print(_.low_res_pos)