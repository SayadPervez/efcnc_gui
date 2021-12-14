import numpy as np
import collections as c

# pospl -> POSition Point Line
def pospl(pt1,pt2,pt3):
    '''
    Returns the position of the point pt3 according to the line vector pt1->pt2\n
    right hand fold => 1\n
    left hand fold => -1\n
    same line      =>  0
    '''
    x1,y1=pt1
    x2,y2=pt2
    xA,yA=pt3

    v1 = (x2-x1, y2-y1)   # Vector 1
    v2 = (x2-xA, y2-yA)   # Vector 2
    xp = v1[0]*v2[1] - v1[1]*v2[0]

    if(xp > 0):
        return(-1)#print('left hand fold')
    elif(xp < 0):
        return(1)#print('right hand fold')
    else:
        return(0)#print('same line')

# evenize -> makes arrays even in size for rotation compatibility
def evenize(a2dlist):
    '''
    Input and output are 2D list.
    If number of rows or columns is not even, this function fixes it.
    Used to achieve bug free rotation
    '''
    i,j = len(a2dlist),len(a2dlist[0])
    if(i%2==0 and j%2==0):
        return(a2dlist)
    if(i%2!=0):
        # if number of rows (height) is not even
        min_index = int(min([sum(_) for _ in a2dlist]))
        del(a2dlist[min_index])
        ret=a2dlist
    if(j%2!=0):
        # if number of cols (width) is not even
        a = a2dlist.copy()
        x = np.array(a).T.tolist()
        min_index = int(min([sum(_) for _ in x]))
        del(x[min_index])
        ret = np.array(x).T.tolist()
    return(ret)

def imgTrim(canva):
    if("shapes" in str(type(canva))):
        canva=canva.shapeMatrix
    r=np.array(canva,dtype=int)
    res=np.where(r==1)
    top=min(res[1])
    bottom=max(res[1])
    right=max(res[0])
    left=min(res[0])
    rotated=r[left:right+1,top:bottom+1]
    rotated = np.array(rotated,dtype=int)
    return(rotated.tolist())

def singleFit(canvas,objectList):
    returnDict = {}
    if(type(objectList)!=type([])):
        objectList = [objectList]
    for obj in objectList :
        cl,cb = canvas.shapeFrameDimension
        chypotunes = (cl**2 + cb**2)**0.5
        ol,ob = obj.shapeFrameDimension
        if(ol > cl and ob > cb):
            returnDict[obj]=(False,False)
        elif (ol <= cl and ob <= cb):
            returnDict[obj]=(True,0)
        elif (ol <= cl and ob > cb and ob <= cl and ol <= cb) or (ol > cl and ob <= cb and ol <= cb and ob <= cl):
            returnDict[obj]=(True,90)
        else:
            returnDict[obj]=(False,False)
    return(returnDict,objectList)

def fitAll(canvas,objectList):
    '''
    This is a theoretical calculation and can sometimes fail to give practical results
    '''
    if(type(objectList)!=type([])):
        objectList = [objectList]
    canvasArea = canvas.surfaceArea
    objectArea = sum([_.surfaceArea for _ in objectList])
    return(True if canvasArea >= objectArea else False)

def sortSurfaceArea(objectList):
    if(type(objectList)!=type([])):
        objectList = [objectList]
    ret = {}
    for obj in objectList:
        ret[obj] = obj.surfaceArea
    ret = dict(sorted(ret.items(),key = lambda item:item[1]))
    return(list(ret.keys())[::-1])

def sortEdgeCorners(objectList):
    if(type(objectList)!=type([])):
        objectList = [objectList]
    ret = {}
    for obj in objectList:
        ret[obj] = {"sa":obj.surfaceArea,"cc":obj.cornerCompatible}
    ret = dict(sorted(ret.items(),key = lambda item:item[1]["cc"]))
    return(list(ret.keys())[::-1])

def isInterfering(c):
    x = c.reshape(-1)
    x = x.tolist()
    if(sum(i>1 for i in x)>0):
        return(True)
    else:
        return(False)

def countShapes(shapeList,myShapeName):
    '''
    count the given type of shape in a given shapeList
    '''
    x = [_.myShape for _ in shapeList]
    return(x.count(myShapeName))

def triangleSort(objectList):
    if(type(objectList)!=type([])):
        objectList = [objectList]
    ret = {}
    for obj in objectList:
        ret[obj] = {"sa":obj.surfaceArea,"cc":obj.triangleCompatible}
    ret = dict(sorted(ret.items(),key = lambda item:item[1]["cc"]))
    return(list(ret.keys())[::-1])

def typeToggle(li):
    retli=[]
    for _ in li:
        try:
            retli.append(float(_))
        except Exception as e:
            retli.append(_)
    return(retli)

def typeToggle2d(li):
    retli=[]
    for row in li:
        retli.append(typeToggle(row))
    return(retli)

def liCompress(li):
    retli = [[str(li[0]),1]]
    for i in range(1,len(li)):
        if(str(li[i])==(retli[-1])[0]):
            (retli[-1])[1]+=1
        else:
            retli.append([str(li[i]),1])
    return(retli)

def liDecompress(li):
    retli = []
    for subList in li:
        retli+=([subList[0]]*subList[1])
    return(typeToggle(retli))

def toggle2dArray(arr2d):
    '''
    Toggles row major 2D array to column major and vice-versa
    '''
    return(np.array(arr2d).T.tolist())

def npAnalyse(nparray,display=True):
    if(display):
        print(c.Counter((nparray.reshape(-1)).tolist()))
    else:
        return(c.Counter((nparray.reshape(-1)).tolist()))

def liAnalyse(li,display=True):
    nparray = np.array(li)
    if(display):
        print(c.Counter((nparray.reshape(-1)).tolist()))
    else:
        return(c.Counter((nparray.reshape(-1)).tolist()))

def outlineBugFixFunction(li2d):
    retli=[]
    for row in li2d:
        templi=[]
        for col in row:
            if(col==''):
                templi.append('0.7')
            else:
                templi.append(col)
        retli.append(templi)
    return(retli)

def binaryFilter(canvas):
    if(type(canvas)==type((1,2,3))):
        canvas,optionalShapeList = canvas[0],canvas[1]
    a = np.array(canvas)
    a[a==1]=1
    a[a!=1]=0
    if(optionalShapeList!=None):
        return((np.array(a,int)).tolist(),optionalShapeList)
    return((np.array(a,int)).tolist())