x_cent=int(input("Enter x-cordinate of centre : "))
y_cent=int(input("Enter x-cordinate of centre : "))
r=int(input("Enter radius of the circle: "))
x=0
y=r
p=5/4-r

x_quad1=[]
y_quad1=[]
while x<y:
    x_quad1.append(x)
    y_quad1.append(y)
    if p<0:
        x += 1
        p = p+2*x+1
    else:
        x += 1
        y -= 1
        p= p+2*x-2*y+1

# append the final points        
x_quad1.append(x)
y_quad1.append(y)
for i in range(len(x_quad1)):
    x_quad1.append(y_quad1[i])
    y_quad1.append(x_quad1[i])
    
x_quad1=[(x_cent+x) for x in x_quad1]
y_quad1=[(y_cent+y) for y in y_quad1]

x_quad2=[(x_cent-x) for x in x_quad1]
y_quad2=[(y_cent+y) for y in y_quad1]


x_quad3=[(x_cent-x) for x in x_quad1]
y_quad3=[(y_cent-y) for y in y_quad1]


x_quad4=[(x_cent+x) for x in x_quad1]
y_quad4=[(y_cent-y) for y in y_quad1]

import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)

plt.plot(x_quad1,y_quad1,x_quad2,y_quad2,x_quad3,y_quad3,x_quad4,y_quad4)

ax.set_aspect('equal')
plt.title("Mid-point circle algorithm")

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.show()