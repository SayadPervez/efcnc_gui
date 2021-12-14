from functions import *
import constants as const
from math import sin,cos,radians,pi
from visualization import arr2png, png2arr,rotate,s2p
from random import randint as ri
import svgBuilder

class CutSheet:
    '''
    Give side in milli-meter( mm ) and angle in degrees( ° )
    '''
    def __init__(self,length,height,angle,uid):
        self.uid = uid
        self.myShape="CutSheet"
        self.length = length
        self.height = height
        self.surfaceArea = length*height
        self.angle = 0
        self.cornerCompatible = 1
        self.triangleCompatible = 0
        self.pngPath = f"{uid}.png"
        self.svgPath = f"{uid}.svg"
        self.__generateShape__(length,height,angle,uid)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nSide Length \t: {self.length} mm\nSide Width \t: {self.width} mm\nShape Tilt \t: {self.angle} °\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def print(self):
        '''
        Prints Object parameters to console
        '''
        print(repr(self))

    def tilt(self,angle):#change.......
        self.angle += angle
        self.shapeMatrix=rotate(evenize(self.shapeMatrix),angle)
        self.shapeFrameDimension = [len(self.shapeMatrix[0]),len(self.shapeMatrix)]

    def displayShape(self):
        '''
        Displays shape as a image
        '''
        (arr2png(self.shapeMatrix)).show()

    def __generateShapeMatrix__(self,length,height,angle,uid):
        '''
        Generates 2D binary shape matrix
        '''
        self.dimensions=[length,height,angle,'mm,mm,°']     # only angle of dimension changes on tilting
        svgBuilder.Rectangle(length,height,angle,f"./IMG/{uid}.svg")
        s2p(f"./SVG/{uid}.svg",f"./IMG/{uid}.png")
        self.shapeMatrix = png2arr(f"./IMG/{uid}.png")
        print(np.shape(self.shapeMatrix))