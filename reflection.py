# Reflect the diamond shaped polygon whose vertices are A(-1,0), B(0,-2), C(1,0) and D(0,2)
# about
# (a) The horizontal line y=2
# (b) The line y=3x+4 

import matplotlib.pyplot as plt
import numpy as np


# x1=int(input("x1: "))
# y1=int(input("y1: "))
# x2=int(input("x2: "))
# y2=int(input("y2: "))
# x3=int(input("x3: "))
# y3=int(input("y3: "))


def part_a():

    x1=-1
    x2=0    
    x3=1
    x4=0

    y1=0
    y2=-2
    y3=0
    y4=2

    X=[x1,x2,x3,x4,x1]
    Y=[y1,y2,y3,y4,y1]

    plt.plot(X,Y)
    plt.show()

    x_trans = 0    
    y_trans = 2  

    T1=[[1,0,-x_trans],
        [0,1,-y_trans],
        [0,0,1]]

    x_reflection = 1
    y_reflection = -1   

    T2=[[x_reflection,0,0],
        [0,y_reflection,0],
        [0,0,1]]

    
    T3=[[1,0,x_trans],
        [0,1,y_trans],
        [0,0,1]]

    t = np.dot(T3,T2)
    T = np.dot(t,T1)
    X_new = []
    Y_new = []

    print(T)

    for i in range(len(X)):
        B=[X[i],Y[i],1]
        R=np.dot(T,B)
        print(R)
        X_new.append(R[0])
        Y_new.append(R[1])
        
    print(X_new,Y_new)

    fig = plt.figure()
    

    plt.plot(X,Y,X_new,Y_new)
    plt.show()




def part_b():
    
    x1=-1
    x2=0
    x3=1
    x4=0

    y1=0
    y2=-2
    y3=0
    y4=2

    X=[x1,x2,x3,x4,x1]
    Y=[y1,y2,y3,y4,y1]

    plt.plot(X,Y)
    plt.show()

    x_trans = 0
    y_trans = 4

    T1=[[1,0,-x_trans],
        [0,1,-y_trans],
        [0,0,1]]


    slope = 3 

    T2=[[0,slope,0],
        [slope,0,0],
        [0,0,1]]

    T3=[[1,0,x_trans],
        [0,1,y_trans],
        [0,0,1]]

    t = np.dot(T3,T2)
    T = np.dot(t,T1)
    X_new = []
    Y_new = []

    print(f"{T}\n" )

    for i in range(len(X)):
        B=[X[i],Y[i],1]
        R=np.dot(T,B)
        print(R)
        X_new.append(R[0])
        Y_new.append(R[1])
        
    print(X_new,Y_new)

    fig = plt.figure()

    plt.plot(X,Y,X_new,Y_new)
    plt.show()



part_b()

