import matplotlib.pyplot as plt

xr1=1000
yr1=-3000
l=2000
w=3000

Xr=[xr1,xr1+l,xr1+l,xr1,xr1]
Yr=[yr1,yr1,yr1+w,yr1+w,yr1]


x1t=1000
y1t=0000
x2t=2000
y2t=2000
x3t=3000
y3t=0000
Xt=[x1t,x2t,x3t,x1t]
Yt=[y1t,y2t,y3t,y1t]





### Data input
x_cent = 2000
y_cent = 1000
r = 260





### Initializations
x_quad1 = []
y_quad1 = []
decor = []


### Step 01
x_init = 0
y_init = r


### Step 02
decision_parameter = 3 - 2*r


### Step 03: First octant
x = x_init
y = y_init
p = decision_parameter

while(x < y):
  
    if p < 0:
        x += 1
        p += 6 + 4 * x
    else:
        x += 1
        y -= 1
        p += 10 - 4 * y + 4 * x
    x_quad1.append(x)
    y_quad1.append(y)
    


x_oct2=[]
y_oct2=[]
# append the second octant to the first quadrant
for i in range(len(x_quad1)):
    x_oct2.append(y_quad1[i])
    y_oct2.append(x_quad1[i])
    
x_oct2.reverse()
y_oct2.reverse()

for i in range(len(x_quad1)):
    x_quad1.append(x_oct2[i])
    y_quad1.append(y_oct2[i])
    


# Second Quadrant, WRT center coordinates
x_quad2 = [(x_cent - x) for x in x_quad1]
y_quad2 = [(y_cent + y) for y in y_quad1]

# Third Quadrant, WRT center coordinates
x_quad3 = [(x_cent - x) for x in x_quad1]
y_quad3 = [(y_cent - y) for y in y_quad1]

# Fourth Quadrant, WRT center coordinates
x_quad4 = [(x_cent + x) for x in x_quad1]
y_quad4 = [(y_cent - y) for y in y_quad1]

# First Quadrant, WRT center coordinates
x_quad1 = [(x_cent + x) for x in x_quad1]
y_quad1 = [(y_cent + y) for y in y_quad1]




plt.plot(Xr,Yr,Xt,Yt,x_quad1, y_quad1, x_quad2, y_quad2, x_quad3, y_quad3, x_quad4, y_quad4)
plt.show()
