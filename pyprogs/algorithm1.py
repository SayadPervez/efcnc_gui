import functions as func
import numpy as np
from math import ceil
from winsound import Beep as beep

def fitting(canvas,shapeList,col=True,log_=False,constCompute=False):
    if(type(constCompute)==type(100)):
        pass
    elif(type(constCompute)==type(True) and constCompute==True):
        constCompute = 100
    else:
        constCompute = False
    cArray = np.array(canvas.shapeMatrix,dtype=float) #cArray => canvasArray
    cx,cy = np.shape(cArray)
    stepX = ceil(cx/constCompute) if constCompute else 1
    stepY = ceil(cy/constCompute) if constCompute else 1
    memoryX = 0
    memoryY = 0
    if(col==False):
        for shape in shapeList:
            sArray = np.array(shape.shapeMatrix,dtype=float)
            sx,sy = np.shape(sArray)
            newCanvas = np.copy(cArray)
            for row in range(0,cx-sx,stepX):
                doublebreak=False
                for col in range(0,cy-sy,stepY):
                    if(row<memoryX and col<memoryY):
                        continue
                    newCanvas = np.copy(cArray)
                    newCanvas[row:row+sx,col:col+sy]+=sArray
                    if(func.isInterfering(newCanvas)):
                        pass
                    else:
                        doublebreak=True
                        shape.low_res_pos = [round(row/cx*100,2),round(col/cy*100,2),0]
                        memoryX=row+(71/100*sx)
                        memoryY=col+(71/100*sy)
                        break
                if(doublebreak==True):
                    break
            cArray = np.copy(newCanvas)
            if(log_):
                print(f"Completed placing {shape.myShape}")
    else:
        for shape in shapeList:
            sArray = np.array(shape.shapeMatrix,dtype=float)
            sx,sy = np.shape(sArray)
            newCanvas = np.copy(cArray)
            for col in range(0,cy-sy,stepY):
                #print("COL --->>>"+str(col))
                doublebreak=False
                for row in range(0,cx-sx,stepX):
                    if(row<memoryX and col<memoryY):
                        continue
                    newCanvas = np.copy(cArray)
                    #print(row)
                    newCanvas[row:row+sx,col:col+sy]+=sArray
                    if(func.isInterfering(newCanvas)):
                        pass
                    else:
                        doublebreak=True
                        shape.low_res_pos = [round(col/cy*100,2),round(row/cx*100,2),0]
                        memoryX=row+(71/100*sx)
                        memoryY=col+(71/100*sy)
                        break
                if(doublebreak==True):
                    break
            cArray = np.copy(newCanvas)
            if(log_):
                print(f"Completed placing {shape.myShape}")
                beep(4000,1000)
    ret = cArray.tolist()
    return(ret)

def run(canvas,shapeList,col=True,log_=False,timeComplexity=False,constCompute=False,memory_=False,noSort=False,returnOrder=False):
    if(noSort==False):
        if(timeComplexity==True or memory_==True):
            shapeList=func.sortSurfaceArea(shapeList)[::-1]
        else:
            shapeList=func.sortSurfaceArea(shapeList)
    d,_=func.singleFit(canvas,shapeList)
    l1 = [d[_][0] for _ in d]
    if(all(l1)==False):
        tooLarge=[]
        for _ in shapeList:
            if(d[_.uid][0]==False):
                tooLarge.append((_.uid,_.myShape,_.dimensions))
        raise Exception(f"{tooLarge} shapes are too large to fit the given canvas...")
    # If program passes till here, 
    # All the given shapes can individually fit in the given canvas.
    if(func.fitAll(canvas,shapeList)==False):
        raise Exception(f"Fitting all shapes in the given canvas is mathematically impossible.")
    # If program passes till here,
    # All the given shapes can be theoretically arranged in the canvas. Practically, I doubt it
    #print(d)
    if(returnOrder):
        return(fitting(canvas,shapeList,col,log_,constCompute),shapeList)
    return(fitting(canvas,shapeList,col,log_,constCompute))
