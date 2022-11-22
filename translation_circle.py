import matplotlib.pyplot as plt


# Data input
x_cent1 = 0
y_cent1 = 0
r = 1000


# Initializations
x1_quad1 = []
y1_quad1 = []
decor = []


# Step 01
x1_init = 0
y1_init = r


# Step 02
decision_parameter = 3 - 2*r


# Step 03: First octant
x1 = x1_init
y1 = y1_init
p = decision_parameter

while(x1 < y1):

    if p < 0:
        x1 += 1
        p += 6 + 4 * x1
    else:
        x1 += 1
        y1 -= 1
        p += 10 - 4 * y1 + 4 * x1
    x1_quad1.append(x1)
    y1_quad1.append(y1)


x1_oct2 = []
y1_oct2 = []
# append the second octant to the first quadrant
for i in range(len(x1_quad1)):
    x1_oct2.append(y1_quad1[i])
    y1_oct2.append(x1_quad1[i])

x1_oct2.reverse()
y1_oct2.reverse()

for i in range(len(x1_quad1)):
    x1_quad1.append(x1_oct2[i])
    y1_quad1.append(y1_oct2[i])


# Second Quadrant, WRT center coordinates
x1_quad2 = [(x_cent1 - x1) for x1 in x1_quad1]
y1_quad2 = [(y_cent1 + y1) for y1 in y1_quad1]

# Third Quadrant, WRT center coordinates
x1_quad3 = [(x_cent1 - x1) for x1 in x1_quad1]
y1_quad3 = [(y_cent1 - y1) for y1 in y1_quad1]

# Fourth Quadrant, WRT center coordinates
x1_quad4 = [(x_cent1 + x1) for x1 in x1_quad1]
y1_quad4 = [(y_cent1 - y1) for y1 in y1_quad1]

# First Quadrant, WRT center coordinates
x1_quad1 = [(x_cent1 + x1) for x1 in x1_quad1]
y1_quad1 = [(y_cent1 + y1) for y1 in y1_quad1]


x_cent2 = 1000
y_cent2 = 0


# Initializations
x2_quad1 = []
y2_quad1 = []
decor = []


# Step 01
x2_init = 0
y2_init = r


# Step 02
decision_parameter = 3 - 2*r


# Step 03: First octant
x2 = x2_init
y2 = y2_init
p = decision_parameter

while(x2 < y2):

    if p < 0:
        x2 += 1
        p += 6 + 4 * x2
    else:
        x2 += 1
        y2 -= 1
        p += 10 - 4 * y2 + 4 * x2
    x2_quad1.append(x2)
    y2_quad1.append(y2)


x2_oct2 = []
y2_oct2 = []
# append the second octant to the first quadrant
for i in range(len(x2_quad1)):
    x2_oct2.append(y2_quad1[i])
    y2_oct2.append(x2_quad1[i])

x2_oct2.reverse()
y2_oct2.reverse()

for i in range(len(x2_quad1)):
    x2_quad1.append(x2_oct2[i])
    y2_quad1.append(y2_oct2[i])


# Second Quadrant, WRT center coordinates
x2_quad2 = [(x_cent2 - x2) for x2 in x2_quad1]
y2_quad2 = [(y_cent2 + y2) for y2 in y2_quad1]

# Third Quadrant, WRT center coordinates
x2_quad3 = [(x_cent2 - x2) for x2 in x2_quad1]
y2_quad3 = [(y_cent2 - y2) for y2 in y2_quad1]

# Fourth Quadrant, WRT center coordinates
x2_quad4 = [(x_cent2 + x2) for x2 in x2_quad1]
y2_quad4 = [(y_cent2 - y2) for y2 in y2_quad1]

# First Quadrant, WRT center coordinates
x2_quad1 = [(x_cent2 + x2) for x2 in x2_quad1]
y2_quad1 = [(y_cent2 + y2) for y2 in y2_quad1]


fig = plt.figure()

plt.plot(x1_quad1, y1_quad1, x1_quad2, y1_quad2, x1_quad3, y1_quad3, x1_quad4, y1_quad4,
         x2_quad1, y2_quad1, x2_quad2, y2_quad2, x2_quad3, y2_quad3, x2_quad4, y2_quad4)
plt.show()
