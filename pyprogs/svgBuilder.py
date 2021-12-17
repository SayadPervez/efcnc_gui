import os
import cairo
from numpy import pi, sqrt
import bs4 as bs
from math import cos,sin

def mm2pt(x):
    return(x*2.83465)

def svgResize2Drawing(path):
    if("./" in path):
        pass
    else:
        if("/" in path):
            p = path[:path.rindex("/")+1]
            path = path[path.rindex("/")+1:]
        else:
            pass
    os.system(f'inkscape --batch-process --actions="FitCanvasToDrawing;export-filename:{path};export-do;" {path}')

def svgRotate(path,angle):
    if("./" in path):
        pass
    else:
        if("/" in path):
            p = path[:path.rindex("/")+1]
            path = path[path.rindex("/")+1:]
        else:
            pass
    os.system(f'inkscape --batch-process --actions="select-all:all;transform-rotate:{str(-angle)};FitCanvasToDrawing;export-filename:{path};export-do;" {path}')

def createCanvas(width,height,path):
    width = mm2pt(width)
    height = mm2pt(height)
    with cairo.SVGSurface(path, width,height) as surface:
        context = cairo.Context(surface)
        context.scale(700, 700)

def Rectangle(l,b,angle=0,filename=""):
    if(filename==""):
        raise Exception("Empty file name svgBuilder rectangle")
    l = mm2pt(l)
    b = mm2pt(b)
    with cairo.SVGSurface(filename,sqrt(l**2 + b**2) , sqrt(l**2+b**2)) as surface:
        cr = cairo.Context(surface)
        cr.rectangle(0,0,l,b)
        cr.fill()
    svgRotate(filename,angle)

def Circle(radius,filename):
    radius = mm2pt(radius)
    with cairo.SVGSurface(filename,2.5*radius , 2.5*radius) as surface:
        cr = cairo.Context(surface)
        theta1=0
        theta2=2*pi
        cr.arc(radius+2,radius+2,radius,theta1,theta2)
        cr.fill()
    svgResize2Drawing(filename) 

def Cone(height,radius,angle=0,filename=""):
    if(filename==""):
        raise Exception("Empty file name svgBuilder cone")
    radius = mm2pt(radius)
    height = mm2pt(height)
    l=sqrt(radius**2 + height**2)
    theta1=0
    theta2=(radius/l)*(2*pi)
    theta = (radius/l)*(2*180)
    with cairo.SVGSurface(filename,2.5*l,2.5*l) as surface:
        cr = cairo.Context(surface)
        cr.move_to(l+2,l+2)
        cr.arc(l+2,l+2,l,theta1,theta2)
        cr.close_path()
        cr.fill()
    svgRotate(filename,angle+theta/2+90)

def objectExtractor(path):
    with open(path,"r") as f:
        data = f.read()
    file = bs.BeautifulSoup(data, "lxml")
    g1 = file.find("g")
    return(str(g1))

def canvasExtracter(path):
    with open(path,"r") as f:
        data = f.read()
    file = bs.BeautifulSoup(data, "lxml")
    g1 = file.find("g")
    gMain = str(g1)
    half1=(data[:data.index("<g")+gMain.index(">")+1])
    half2=(data[data.index("<g")+gMain.index(">")+1:])
    return(half1,half2)

def svgPlacer(canvas,svgObjects,x,y):
    if(type(svgObjects)==type([])):
        if(not(len(svgObjects)==len(x)==len(y))):
            raise Exception("Unequal Array Length - SVGPLACER")
    else:
        x,y,svgObjects=[x],[y],[svgObjects]
    h1,h2=canvasExtracter(canvas)
    st=""
    for i,svg in enumerate(svgObjects):
        st+=f'<g id="{str(i)}" transform="translate({mm2pt(x[i])},{mm2pt(y[i])})">'+objectExtractor(svg)+"</g>"
    output = h1+st+h2
    with open(canvas,"w") as f:
        f.write(output)

def Sector(radius,sector_angle,angle=0,filename=""):
    if(filename==""):
        raise Exception("Empty file name svgBuilder cone")
    l=mm2pt(radius)
    sector_angle=sector_angle*pi/180
    with cairo.SVGSurface(filename,2.5*l,2.5*l) as surface:
        cr = cairo.Context(surface)
        cr.move_to(l+2,l+2)
        cr.arc(l+2,l+2,l,0,sector_angle)
        cr.close_path()
        cr.fill()
    svgRotate(filename,angle)

def frustum(R,r,h,angle=0,filename=""):
    if(filename==""):
        raise Exception("Empty file name svgBuilder cone")
    R=mm2pt(R)
    r=mm2pt(r)
    h=mm2pt(h)
    t=sqrt(h**2 + (R-r)**2)
    L=t*R/(R-r)
    theta=(R/L)*(2*pi)
    l=L-t
    with cairo.SVGSurface(filename,2.5*L,2.5*L) as surface:
        cr = cairo.Context(surface)
        X1,Y1=xy(L,0)
        X2,Y2=xy(L,theta/2)
        X3,Y3=xy(L,theta)
        x1,y1=xy(l,0)
        x2,y2=xy(l,theta/2)
        x3,y3=xy(l,theta)
        cr.curve_to(X1+L,Y1+L,X2+L,Y2+L,X3+L,Y3+L)
        cr.line_to(x3+L,y3+L)
        cr.curve_to(x3+L,y3+L,x2+L,y2+L,x1+L,y1+L)
        cr.line_to(X1+L,Y1+L)
        cr.fill()
    svgRotate(filename,angle)

def xy(r,theta):
    x=r*cos(theta)
    y=r*sin(theta)
    return x,y

def segment(R,r,segment_angle,angle=0,filename=""):
    if(filename==""):
        raise Exception("Empty file name svgBuilder cone")
    R=mm2pt(R)
    r=mm2pt(r)
    theta=segment_angle*pi/180
    with cairo.SVGSurface(filename,2.5*R,2.5*R) as surface:
        cr = cairo.Context(surface)
        X1,Y1=xy(R,0)
        X2,Y2=xy(R,theta/2)
        X3,Y3=xy(R,theta)
        x1,y1=xy(r,0)
        x2,y2=xy(r,theta/2)
        x3,y3=xy(r,theta)
        cr.curve_to(X1+R,Y1+R,X2+R,Y2+R,X3+R,Y3+R)
        cr.line_to(x3+R,y3+R)
        cr.curve_to(x3+R,y3+R,x2+R,y2+R,x1+R,y1+R)
        cr.line_to(X1+R,Y1+R)
        cr.fill()
    svgRotate(filename,angle,outputFileName=filename)