import matplotlib.pyplot as plt
x1 = float(input('please enter value of x1: ')) 
y1 = float(input('please enter value of y1: '))
x2 = float(input('please enter value of x2: '))
y2 = float(input('please enter value of y2: '))
x,y=x1,y1
dx=x2-x1
dy=y2-y1
m= dy/dx
p=2*dy-dx
X=[x]
Y=[y]
i=1
if m < 1:
    p=2*dy-dx
    while i<=dx:
        if p<0:
            x=x+1
            y=y
            p=p+2*dy
            X.append(x)
            Y.append(y)
        else:
            x=x+1
            y=y+1
            p=p+2*(dy-dx)
            X.append(x)
            Y.append(y)
        i=i+1
else:
    p=2*dx-dy
    while i<=dy:
        if p<0:
            x=x
            y=y+1
            p=p+2*dx
            X.append(x)
            Y.append(y)
        else:
            x=x+1
            y=y+1
            p=p+2*(dx-dy)
            X.append(x)
            Y.append(y)
        i=i+1
        
plt.plot(X,Y)
plt.show()