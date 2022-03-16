import functions as func
import numpy as np
from math import ceil

def fitting(canvas,shapeList,log_=False,constCompute=False):
    cArray = np.array(canvas.shapeMatrix,dtype=float) #cArray => canvasArray
    cx,cy = np.shape(cArray)
    stepX = constCompute if constCompute else 1
    stepY = constCompute if constCompute else 1
    memoryX = 0
    memoryY = 0
    unplacedShapes=[]
    placedShapes=[]
    pseudo_cy = int(ceil(1.7 * np.shape(np.array(shapeList[0].shapeMatrix,dtype=float))[1]))
    for shape in shapeList:
        #print("Pseudo Cx : ",pseudo_cy)
        shapePlaced = False
        sArray = np.array(shape.shapeMatrix,dtype=float)
        sx,sy = np.shape(sArray)
        if(int(sy)>int(pseudo_cy)):
            pseudo_cy += int(ceil(1.4*sy))
        newCanvas = np.copy(cArray)
        for row in range(0,cx-sx,stepX):
            doublebreak=False
            for col in range(0,pseudo_cy-sy,stepY):
                if(row<memoryX and col<memoryY):
                    continue
                newCanvas = np.copy(cArray)
                newCanvas[row:row+sx,col:col+sy]+=sArray
                if(func.isInterfering(newCanvas)):
                    pass
                else:
                    doublebreak=True
                    shapePlaced=True
                    shape.low_res_pos = [round(col/cy*100,2),round(row/cx*100,2),0]
                    memoryX=row+(71/100*sx)
                    memoryY=col+(71/100*sy)
                    break
            if(doublebreak==True):
                break
        if(log_ and shapePlaced):
            print(f"Completed placing {shape.myShape}")
            shape.placed=True
            placedShapes.append(shape)
            cArray = np.copy(newCanvas)
        else:
            unplacedShapes.append(shape)
            shape.placed=False
        #print("\n")
    ret = cArray.tolist()
    return(ret,placedShapes,unplacedShapes)



def run(canvas,shapeList,log_=False,constCompute=False,returnOrder=False):
    shapeList=func.sortA5(shapeList)
    d,_=func.singleFit(canvas,shapeList)
    l1 = [d[_][0] for _ in d]
    try:
        if(all(l1)==False):
            tooLarge=[]
            for _ in shapeList:
                if(d[_.uid][0]==False):
                    tooLarge.append((_.uid,_.myShape,_.dimensions))
    except Exception as e:
        func.pushError(f"* shapes are too large to fit the given canvas...")
        raise Exception(f"{tooLarge} shapes are too large to fit the given canvas...")
    # If program passes till here, 
    # All the given shapes can individually fit in the given canvas.
    if(func.fitAll(canvas,shapeList)==False):
        func.pushError(f"Fitting all shapes in the given canvas is mathematically impossible.")
        raise Exception(f"Fitting all shapes in the given canvas is mathematically impossible.")
    # If program passes till here,
    # All the given shapes can be theoretically arranged in the canvas. Practically, I doubt it
    #print(d)
    for shape in shapeList:
        if(shape.a3compat):
            shape.flaTilt(1)
    return(fitting(canvas,shapeList,log_,constCompute))