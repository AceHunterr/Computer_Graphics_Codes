import matplotlib.pyplot as plt
import math
import fractions
import numpy as np
x1 = int(input("x1="))
x2 = int(input("x2="))
x3 = int(input("x3="))
x4 = int(input("x4="))
y1 = int(input("y1="))
y2 = int(input("y2="))
y3 = int(input("y3="))
y4 = int(input("y4="))
X = [x1, x2, x3, x4, x1]
Y = [y1, y2, y3, y4, y1]
plt.plot(X, Y)
plt.show()

c = int(input("c="))
# tranlation origin
T1 = [[1, 0, 0],
      [0, 1, c],
      [0, 0, 1]]
m = float(input("m="))
theta = math.atan(m)
s = math.sin(math.radians(theta))
co = math.cos(math.radians(theta))
# clockwise
T2 = [[co, s, 0],
      [-s, co, 0],
      [0, 0, 1]]
# reflection about x axis
T3 = [[-1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]]
# inverse rotation
T4 = [[co, -s, 0],
      [s, co, 0],
      [0, 0, 1]]
# inverse translation
T5 = [[1, 0, 0],
      [0, 1, -c],
      [0, 0, 1]]
T6 = np.dot(T5, T4)
T7 = np.dot(T6, T3)
T8 = np.dot(T7, T4)
T9 = np.dot(T8, T5)

X_new = []
Y_new = []

for i in range(len(X)):
    B = [X[i], Y[i], 1]
    T = np.dot(T9, B)
    X_new.append(T[0])
    Y_new.append(T[1])

fig = plt.figure()
plt.plot(X, Y, X_new, Y_new)
plt.show()
