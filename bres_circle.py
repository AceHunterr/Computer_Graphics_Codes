import matplotlib.pyplot as plt


### Data input
x_cent = int(input("Enter x-coordinates of the center: "))
y_cent = int(input("Enter y-coordinates of the center: "))
r = int(input("Enter the radius of the circle: "))

 

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




### Step 04
fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(x_quad1, y_quad1, x_quad2, y_quad2, x_quad3, y_quad3, x_quad4, y_quad4)

ax.set_aspect('equal', adjustable='box')

plt.title("Bresenham Circle Drawing Algorithm")

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()