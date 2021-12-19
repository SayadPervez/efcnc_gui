from functions import *
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
        self.__generateShape__(length,height,angle)

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
        self.shapeMatrix = p2aBugFixFunction(png2arr(self.pngPath))
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
        self.dimensions=[self.radius,'mm']
        svgBuilder.Circle(radius,self.svgPath)
        s2p(self.svgPath,self.pngPath)
        tranparencyFilter(self.pngPath)
        self.shapeMatrix = p2aBugFixFunction(png2arr(self.pngPath))
        self.shapeFrameDimension=list(np.shape(self.shapeMatrix))

class Cone:
    '''
    Give cone-height & cone-radius in milli-meter( mm )
    '''
    def __init__(self,cone_height,cone_radius,angle,uid):
        self.uid = uid
        self.pngPath = f"./PNG/{uid}.png"
        self.svgPath = f"./SVG/{uid}.svg"
        self.myShape="cone"
        self.angle = 0
        self.cone_radius = round(cone_radius)
        self.cone_height = round(cone_height)
        self.slantHeight = round((cone_radius**2 + cone_height**2)**0.5)
        self.theta = 2*180*cone_radius/self.slantHeight
        self.surfaceArea = pi*(self.slantHeight**2)*self.theta/360
        self.cornerCompatible = 0
        self.flatAngle = ((180 - self.theta)/2)+self.theta
        #print('theta = ',self.theta)
        if(self.theta>=360):
            raise Exception("Illegal cone dimensions.")
            return(0)
        self.cone_type = 1 if self.theta<=180 else 2
        self.triangleCompatible = 3 if self.cone_type==1 else 2
        self.__generateShapeMatrix__(cone_height,cone_radius,angle)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nObject UID \t: {self.uid}\nShape Radius \t: {self.cone_radius} mm\nShape Height \t: {self.cone_height} mm\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def tilt(self,angle):
        self.angle = angle
        self.shapeMatrix=rotate(evenize(self.shapeMatrix),angle)
        self.shapeFrameDimension = [len(self.shapeMatrix[0]),len(self.shapeMatrix)]

    def flaTilt(self,direction=1):
        self.shapeMatrix = evenize(self.shapeMatrix)
        if(self.cone_type==1):
            self.tilt((direction/abs(direction))*self.flatAngle)
        else:
            self.tilt(180)

    def print(self):
        '''
        Prints Object parameters to console
        '''
        print(repr(self))

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
        if( (ptX-radius)**2 + (ptY-(self.width*const.sampl/2))**2 <= radius**2 ):
            return(True)
        else:
            return(False)

    def __generateShapeMatrix__(self,height,radius,angle):
        '''
        Generates 2D binary shape matrix
        '''
        self.dimensions=[height,radius,angle,'mm,mm,°']     # only angle of dimension changes on tilting
        svgBuilder.Cone(height,radius,angle,self.svgPath)
        s2p(self.svgPath,self.pngPath)
        tranparencyFilter(self.pngPath)
        self.shapeMatrix = p2aBugFixFunction(png2arr(self.pngPath))
        self.shapeFrameDimension=list(np.shape(self.shapeMatrix))

class Canvas:
    '''
    Give side in milli-meter( mm )
    '''
    def __init__(self,length,height):
        self.uid = "Canvas"
        self.myShape="Canvas"
        self.length = length
        self.height = height
        self.surfaceArea = length*height
        self.pngPath = f"./PNG/{self.uid}.png"
        self.svgPath = f"./SVG/{self.uid}.svg"
        self.__generateShape__(length,height)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nObject UID \t: {self.uid}\nSide Length \t: {self.length} mm\nSide Height \t: {self.height} mm\nShape Tilt \t: {self.angle} °\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
    def print(self):
        '''
        Prints Object parameters to console
        '''
        print(repr(self))

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

    def __generateShape__(self,length,height):
        '''
        Generates 2D binary shape matrix
        '''
        self.dimensions=[length,height,'mm,mm']
        svgBuilder.createCanvas(length,height,self.svgPath)
        s2p(self.svgPath,self.pngPath)
        tranparencyFilter(self.pngPath)
        self.shapeMatrix = p2aBugFixFunction(png2arr(self.pngPath))
        self.shapeFrameDimension=list(np.shape(self.shapeMatrix))

class Custom:
    '''
    Give side in milli-meter( mm )
    '''
    def __init__(self,filecontents,uid):
        self.uid = uid
        self.myShape="Custom"
        self.fileContents = filecontents
        self.angle = 0
        self.pngPath = f"./PNG/{self.uid}.png"
        self.svgPath = f"./SVG/{self.uid}.svg"
        self.__generateShape__(filecontents)

    def __repr__(self):
        return(f"Object Shape \t: {self.myShape}\nObject UID \t: {self.uid}\nShape Tilt \t: {self.angle} °\nshapeFrameDimension \t: {self.shapeFrameDimension}")
    
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

    def __generateShape__(self,fc):
        '''
        Generates 2D binary shape matrix
        '''
        with open(self.svgPath,"w") as f:
            f.write(fc)
        s2p(self.svgPath,self.pngPath)
        tranparencyFilter(self.pngPath)
        self.shapeMatrix = p2aBugFixFunction(png2arr(self.pngPath))
        self.shapeFrameDimension=list(np.shape(self.shapeMatrix))
        self.surfaceArea = self.shapeFrameDimension[0]*self.shapeFrameDimension[1]