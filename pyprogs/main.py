from shapeManager import *
from functions import *
import algorithm1,algorithm2,algorithm3,algorithm4
from visualization import *
import sys
from json import loads as jsonparser

def RUN(jsonString):
    print(type(jsonparser(jsonString)))

if len(sys.argv)>1:
    RUN((sys.argv[1]).replace("^",'"'))