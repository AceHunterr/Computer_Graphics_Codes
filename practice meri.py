import matplotlib.pyplot as plt

x1= float(input("Enter the value of x1"))
y1= float(input("Enter the value of x1"))
x2= float(input("Enter the value of x1"))
y2= float(input("Enter the value of x1"))

dx=x2-x1
dy=y2-y1
if abs(dx)>abs(dy):
    step=abs(dx)
else:
    step=abs(dy)
xinc=dx/step
yinc=dy/step
X=[x1]
Y=[y1]
i=0
while i<step:
  i+=1
  x1=x1+xinc
  y1=y1+yinc
  X.append(x1)
  Y.append(y1)
plt.plot(X,Y)
plt.show()

  

   
