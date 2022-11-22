import matplotlib.pyplot as plt

# Translation of a rectangle


x1=int(input("x1: "))
y1=int(input("y1: "))
l=int(input("lenghth: "))
w=int(input("width: "))
# x3=int(input("x3: "))
# y3=int(input("y3: "))
# x4=int(input("x4: "))
# y4=int(input("y4: "))
X=[x1,x1+l,x1+l,x1,x1]
Y=[y1,y1,y1+w,y1+w,y1]
plt.plot(X,Y)
plt.show()


#Translation
x_trans=int(input("x-coordinate "))
y_trans=int(input("y-coordinate "))


import numpy as np 



X_new=[]
Y_new=[]

T=[[1, 0, x_trans],
   [0, 1, y_trans],
    [0, 0, 1]]

R=[0, 0, 0]

            
for i in range(len(X)):
    B=[X[i],Y[i],1]
    R=np.dot(T,B)
    X_new.append(R[0])
    Y_new.append(R[1])
    
    
    
print(X_new)
print(Y_new)


fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(X,Y,X_new,Y_new)
plt.show()