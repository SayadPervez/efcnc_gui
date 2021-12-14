from functions import *
import constants as const
from math import sin,cos,radians,pi
from visualization import arr2png, png2arr,rotate,s2p,showPNG,tranparencyFilter
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
        self.pngPath = f"./PNG/{uid}.png"
        self.svgPath = f"./SVG/{uid}.svg"
        self.__generateShape__(length,height,angle,uid)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nObject UID \t: {self.uid}\nSide Length \t: {self.length} mm\nSide Height \t: {self.height} mm\nShape Tilt \t: {self.angle} °\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def print(self):
        '''
        Prints Object parameters to console
        '''
        print(repr(self))

    def tilt(self,angle):
        self.angle += angle
        self.shapeMatrix=rotate(evenize(self.shapeMatrix),angle)
        self.shapeFrameDimension = [len(self.shapeMatrix[0]),len(self.shapeMatrix)]

    def displayShape(self):
        '''
        Displays shape as a image
        '''
        (arr2png(self.shapeMatrix)).show()

    def printShape(self):
        '''
        Prints shape to console in binary 

        #### Warning : CPU intensive task
        '''
        temp = ""
        for li in self.shapeMatrix:
            for num in li:
                temp+=str(num)
            temp+="\n"
        print(temp)

    def __generateShape__(self,length,height,angle):
        '''
        Generates 2D binary shape matrix
        '''
        self.dimensions=[length,height,angle,'mm,mm,°']
        svgBuilder.Rectangle(length,height,angle,self.svgPath)
        s2p(self.svgPath,self.pngPath)
        tranparencyFilter(self.pngPath)
        self.shapeMatrix = png2arr(self.pngPath)
        self.shapeFrameDimension=list(np.shape(self.shapeMatrix))

class Circle:
    '''
    Give radius in milli-meter( mm )
    '''
    def __init__(self,radius,uid):
        self.uid = uid
        self.myShape="Circle"
        self.radius = radius
        self.cornerCompatible = 0
        self.triangleCompatible = 1
        self.surfaceArea = pi*radius*radius
        self.pngPath = f"./PNG/{uid}.png"
        self.svgPath = f"./SVG/{uid}.svg"
        self.__generateShapeMatrix__(radius)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nObject UID \t: {self.uid}\nShape Radius \t: {self.radius} mm\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def print(self):
        '''
        Prints Object parameters to console
        '''
        print(repr(self))

    def tilt(self,angle):
        _=angle
        pass

    def printShape(self):
        '''
        Prints shape to console in binary 

        #### Warning : CPU intensive task
        '''
        temp = ""
        for li in self.shapeMatrix:
            for num in li:
                temp+=str(num)
            temp+="\n"
        print(temp)

    def displayShape(self):
        '''
        Displays shape as a image
        '''
        (arr2png(self.shapeMatrix)).show()
    
    def isPointInCircle(self,ptX,ptY,radius):
        if( (ptX-radius)**2 + (ptY-radius)**2 <= radius**2 ):
            return(True)
        else:
            return(False)

    def __generateShapeMatrix__(self,radius):
        '''
        Generates 2D binary shape matrix
        '''
        self.dimensions=[self.radius,'mm']     # only angle of dimension changes on tilting
        svgBuilder.Circle(radius,self.svgPath)
        s2p(self.svgPath,self.pngPath)
        tranparencyFilter(self.pngPath)
        self.shapeMatrix = png2arr(self.pngPath)
        self.shapeFrameDimension=list(np.shape(self.shapeMatrix))