import sys
sys.path.insert(0, '/home/niketh/matgeo/codes/CoordGeo')
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

from line.funcs import *
from triangle.funcs import *

data = np.loadtxt("values.dat", skiprows=1)

xc = data[0]
yc = data[1]

A = np.array(([6, 5])).reshape(-1, 1)
B = np.array(([-4, 3])).reshape(-1, 1)
P = np.array(([xc, yc])).reshape(-1, 1)

midpoint = (A + B) / 2
slope_AB = (B[1][0] - A[1][0]) / (B[0][0] - A[0][0])
slope_perpendicular = -1 / slope_AB if slope_AB != 0 else float('inf')

x_values = np.linspace(-10, 10, 100)
y_values_AB = slope_AB * (x_values - A[0][0]) + A[1][0]

if slope_perpendicular != float('inf'):
    y_values_perpendicular = slope_perpendicular * (x_values - midpoint[0]) + midpoint[1]
else:
    y_values_perpendicular = np.full_like(x_values, midpoint[1])

plt.figure(figsize=(10, 6))

plt.plot(x_values, y_values_AB, label='Line AB', color='blue')
plt.plot(x_values, y_values_perpendicular, label='Perpendicular Bisector', color='green', linestyle='dotted')

plt.scatter([A[0][0], B[0][0], P[0][0]], [A[1][0], B[1][0], P[1][0]], color='red', s=20, zorder=5)

plt.text(A[0][0] + 0.5, A[1][0], f' A ({A[0][0]}, {A[1][0]})', fontsize=10, ha='left', color='black')
plt.text(B[0][0] - 0.5, B[1][0], f' B ({B[0][0]}, {B[1][0]})', fontsize=10, ha='right', color='black')
plt.text(P[0][0] + 0.5, P[1][0], f' P ({P[0][0]}, {P[1][0]})', fontsize=10, ha='left', color='black')

plt.legend(loc='upper left', fontsize=10)

ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.grid()
plt.axis('equal')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

