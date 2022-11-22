import matplotlib.pyplot as plt
import math

import numpy as np

# numpy to handle the arrays or matrix
x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))
x3=int(input("x3: "))
y3=int(input("y3: "))
x4=int(input("x4: "))
y4=int(input("y4: "))
X = [x1, x2, x3, x4 , x1]
Y = [y1, y2, y3, y4 , y1]


# translate
theta = float(input("Enter rotating variable "))

s = math.sin(math.radians(theta))
c = math.cos(math.radians(theta))

x_trans=int(input("fixed point x coordinate: "))
y_trans=int(input("fixed point y coordinate: "))
X_new=[]
Y_new=[]

T1=[[1,0,-x_trans],
   [0,1,-y_trans],
   [0,0,1]]

T2=[[c,-s,0],
    [s,c,0],
    [0,0,1]]

T3=[[1,0,x_trans],
   [0,1,y_trans],
   [0,0,1]]

t = np.dot(T3,T2)
T = np.dot(t,T1)
X_new = []
Y_new = []



R = [0, 0, 0]


for i in range(len(X)):
    B = [X[i], Y[i], 1]
    R = np.dot(T, B)
    X_new.append(R[0])
    Y_new.append(R[1])

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(X, Y, X_new, Y_new)
plt.show()