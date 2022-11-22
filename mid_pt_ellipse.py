x_cent=int(input("x-coordinate of center"))
y_cent=int(input("y-coordinate of center"))
a=int(input("minor axis: "))
b=int(input("major axis: "))
x=0
y=b
d1= b*b-a*a*b+0.25*a*a
x_quad1=[]
y_quad1=[]
print(d1)
while(a*a*(y-0.5)>b*b*(x+1)):
    if(d1<0):
        d1=d1+b*b*(2*x+3)
        print(d1)
    else:
        d1=d1+b*b*(2*x+3)+a*a*(2-2*y)
        print(d1)
        y=y-1
    x=x+1
    print(x,y)
    x_quad1.append(x)
    y_quad1.append(y)
    d2=b*b*(x+0.5)*(x+0.5)+a*a*(y-1)*(y-1)-a*a*b*b
print(d2)
while(y>0):
    if(d2<0):
        d2=d2+b*b*(2*x+3)+a*a*(3-2*y)
        x=x+1
        print(d2)
    else: 
        d2=d2+a*a*(3-2*y)
        print(d2)
    y=y-1
    x_quad1.append(x)
    y_quad1.append(y)
    print(x,y)
    
x_quad2=[(x_cent-x) for x in x_quad1]
y_quad2=[(y_cent+y) for y in y_quad1]

x_quad3=[(x_cent-x) for x in x_quad1]
y_quad3=[(y_cent-y) for y in y_quad1]

x_quad4=[(x_cent+x) for x in x_quad1]
y_quad4=[(y_cent-y) for y in y_quad1]

x_quad1=[(x_cent+x) for x in x_quad1]
y_quad1=[(y_cent+y) for y in y_quad1]

x_quad1
y_quad1

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')

plt.title("Mid-point ellipse drawing algorithm")

plt.xlabel("x-axis")
plt.ylabel("y-axis")


plt.plot(x_quad1,y_quad1,x_quad2,y_quad2,x_quad3,y_quad3,x_quad4,y_quad4)
plt.show()