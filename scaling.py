import matplotlib.pyplot as plt
import numpy as np


x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))
x3=int(input("x3: "))
y3=int(input("y3: "))
X=[x1,x2,x3,x1]
Y=[y1,y2,y3,y1]
plt.plot(X,Y)
plt.show()
S=int(input("Enter scaling factor "))
x_fix=int(input("x coordinate to be fixed "))
y_fix=int(input("y coordinate to be fixed "))


X_new=[]
Y_new=[]

T=[[1, 0, x_fix],
   [0, 1, y_fix],
    [0, 0, 1]]
S=[[S, 0, 0],
   [0, S, 0],
    [0, 0, 1]]
Tn=[[1, 0, -x_fix],
   [0, 1, -y_fix],
    [0, 0, 1]]

R=[0, 0, 0]
tk=np.dot(T,S)
tf=np.dot(tk,Tn)

            
for i in range(len(X)):
    B=[X[i],Y[i],1]
    R=np.dot(tf,B)
    X_new.append(R[0])
    Y_new.append(R[1])

fig = plt.figure()

plt.plot(X,Y,X_new,Y_new)
plt.show()