from functions import *
from shapes import *
import algorithm1,algorithm2,algorithm3,algorithm4
import constants as const
from visualization import *
import math

def upscale(canvas,shapes,alg=1,scaleFactor=[2,5],constCompute=75,display=False,thickness=1):

    # # Low Resolution Computing :
    # ### Sampling level set to 1
    const.sampl=scaleFactor[0]

    # ## Initializing Shapes and Canvas for low resolution
    canvas.regenerateSelf()
    for shape in shapes:
        shape.regenerateSelf()

    # ## Pre-Processing :
    for shape in shapes:
        shape.shapeMatrix = outline_with_shape(shape,thickness)


    # ## Low Resoultion Computation :
    print("Starting low level algorithm")
    if(alg == 1):
        out,shapes = binaryFilter(algorithm1.run(canvas,shapes,log_=True,constCompute=constCompute,returnOrder=True))
    elif(alg == 2):
        out,shapes = binaryFilter(algorithm2.run(canvas,shapes,log_=True,constCompute=constCompute,returnOrder=True))
    elif(alg == 3):
        out,shapes = binaryFilter(algorithm3.run(canvas,shapes,log_=True,constCompute=constCompute,returnOrder=True))
    elif(alg == 4):
        out,shapes = binaryFilter(algorithm4.run(canvas,shapes,log_=True,constCompute=constCompute,returnOrder=True))
    else:
        raise Exception("Invalid Algorithm")
    print("Lowlevel rendering completed")
    #arr2png(out).show()


    # # High Resolution Rendering :

    # ### Higher Resolution is set
    const.sampl = scaleFactor[1]


    # ### Below block just for name sake
    '''
    for shape in shapes:
        print(shape.low_res_pos)
    '''


    # ## High Resolution Shape Place Function :
    def canvaPut(canvas,shapes):
        canvas.regenerateSelf()
        c = np.array(canvas.shapeMatrix)
        cx,cy = np.shape(c)
        for shape in shapes:
            shape.regenerateSelf()
            s = np.array(shape.shapeMatrix)
            sx,sy = np.shape(s)
            px , py , _ = shape.low_res_pos
            px,py = math.floor(px/100*cx),math.floor(py/100*cy)
            c[px:px+sx,py:py+sy] += s
        return(c)


    out = canvaPut(canvas,shapes)
    if(display):
        arr2png(out).show()
    return(out)


canvas = Canvas(2000,1500)
shapes = [ 
            Square(20) ,
            Rectangle(35,25) , 
            Circle(7) ,
            Cone(17,20) ,
            Cone(12,4),
            Square(3)
        ]
upscale(canvas,shapes,display=True,alg=4,thickness=2,scaleFactor=[2,5])