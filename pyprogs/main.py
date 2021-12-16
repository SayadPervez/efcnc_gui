from shapeManager import CutSheet,Circle,Cone,Canvas
from functions import *
import algorithm1,algorithm2,algorithm3,algorithm4
from visualization import arr2png as a2p

freeSpace()

sheet=CutSheet(30,10,0,"abcdefgh1")
circle = Circle(50,"qwerty1")
cone = Cone(30,10,0,"zxcvb1")
canva=Canvas(1920,1080)

out = algorithm1.run(canva,[sheet,circle,cone],log_=True)
a2p(out).show()