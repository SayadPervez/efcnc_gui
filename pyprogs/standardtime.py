from functions import *
import constants as const
import algorithm1,algorithm2,algorithm3,algorithm4
from visualization import *
from visualization import arr2png as a2p
import time
from matplotlib import pyplot as plt
from shapes import *

if(const.sampl!=10):
    pass
    #raise Exception("\"sampl\" value not set to standard value 10.\nSet \"sampl = 10\" in constants.py to coninue ...")

def alg1Large():
    print("\na1-L starting:")
    canvasLarge = Canvas(1080,720)
    shapesLarge = [ 
                Square(200) ,
                Rectangle(100,250) , 
                Circle(70) ,
                Cone(170,200) ,
                Cone(120,40)
            ]
    s = time.time()
    c = canvasLarge
    li = shapesLarge
    print("Starting algorithm")
    out = algorithm1.run(c,li,log_=True,constCompute=10)
    e = time.time()
    #a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def alg1Small():
    print("\na1-S starting:")
    canvas = Canvas(108,72)
    shapes    = [ 
                Square(20) ,
                Rectangle(10,25) , 
                Circle(7) ,
                Cone(17,20) ,
                Cone(12,4)
            ]
    s = time.time()
    c = canvas
    li = shapes
    print("Starting algorithm")
    out = algorithm1.run(c,li,log_=True,constCompute=100)
    e = time.time()
    #a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def alg2Large():
    print("\na2-L starting:")
    canvasLarge = Canvas(1080,720)
    shapesLarge = [ 
                Square(200) ,
                Rectangle(100,250) , 
                Circle(70) ,
                Cone(170,200) ,
                Cone(120,40)
            ]
    s = time.time()
    c = canvasLarge
    li = shapesLarge
    print("Starting algorithm")
    out = algorithm2.run(c,li,log_=True,constCompute=10)
    e = time.time()
    #a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def alg2Small():
    print("\na2-S starting:")
    canvas = Canvas(108,72)
    shapes    = [ 
                Square(20) ,
                Rectangle(10,25) , 
                Circle(7) ,
                Cone(17,20) ,
                Cone(12,4)
            ]
    s = time.time()
    c = canvas
    li = shapes
    print("Starting algorithm")
    out = algorithm2.run(c,li,log_=True,constCompute=100)
    #out = imgTrim(out)
    e = time.time()
    #a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def alg3Large():
    print("\na3-L starting:")
    canvasLarge = Canvas(1080,720)
    shapesLarge = [ 
                Square(200) ,
                Rectangle(100,250) , 
                Circle(70) ,
                Cone(170,200) ,
                Cone(120,40)
            ]
    s = time.time()
    c = canvasLarge
    li = shapesLarge
    print("Starting algorithm")
    out = algorithm3.run(c,li,log_=True,constCompute=10)
    e = time.time()
    #a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def alg3Small():
    print("\na3-S starting:")
    canvas = Canvas(108,72)
    shapes    = [ 
                Square(20) ,
                Rectangle(10,25) , 
                Circle(7) ,
                Cone(17,20) ,
                Cone(12,4)
            ]
    s = time.time()
    c = canvas
    li = shapes
    print("Starting algorithm")
    out = algorithm3.run(c,li,log_=True,constCompute=100)
    e = time.time()
    #a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def alg4Large():
    print("\na4-L starting:")
    canvasLarge = Canvas(1080,720)
    shapesLarge = [ 
                Square(200) ,
                Rectangle(100,250) , 
                Circle(70) ,
                Cone(170,200) ,
                Cone(120,40)
            ]
    s = time.time()
    c = canvasLarge
    li = shapesLarge
    print("Starting algorithm")
    out = algorithm4.run(c,li,log_=True,constCompute=10)
    e = time.time()
    #a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def alg4Small():
    print("\na4-S starting:")
    canvas = Canvas(108,72)
    shapes    = [ 
                Square(20) ,
                Rectangle(10,25) , 
                Circle(7) ,
                Cone(17,20) ,
                Cone(12,4)
            ]
    s = time.time()
    c = canvas
    li = shapes
    print("Starting algorithm")
    out = algorithm4.run(c,li,log_=True,constCompute=100)
    #out = imgTrim(out)
    e = time.time()
    #a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def RUN():
    x = ['a1-S','a2-S','a3-S','a4-S','a1-L','a2-L','a3-L','a4-L']
    y = []
    y.append(alg1Small())
    #input("Proceed ?? ")
    y.append(alg2Small())
    #input("Proceed ?? ")
    y.append(alg3Small())
    #input("Proceed ?? ")
    y.append(alg4Small())
    #input("Proceed ?? ")
    y.append(alg1Large())
    #input("Proceed ?? ")
    y.append(alg2Large())
    #input("Proceed ?? ")
    y.append(alg3Large())
    #input("Proceed ?? ")
    y.append(alg4Large())
    #input("Proceed ?? ")
    print("Plotting ...")
    plt.bar(x, height=y, alpha=0.8 , color=['green','green','green','green','red','red','red','red'])
    plt.title("Algorithm Comparison for Small and Large Canvas")
    plt.xlabel("Algorithms")
    plt.ylabel("Time taken")
    plt.show()

RUN()
#alg2Large()