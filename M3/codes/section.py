#Code by /sdcard/github/matgeo/codes/CoordGeoVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Secion Formula


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/niketh/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

data = np.loadtxt("values.dat", skiprows=1)  

xc = data[0]# Extract frequency data from values.dat
yc = data[1]# Extract magnitude data from values.dat


#Given points
A = np.array(([6,5])).reshape(-1,1)
B = np.array(([-4,3])).reshape(-1,1)
P = np.array(([xc,yc])).reshape(-1,1)


#Labeling the coordinates
tri_coords = np.block([[A,B,P]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','P']
for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,-10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
# use set_position
ax = plt.gca()
#ax.spines['top'].set_color('none')
#ax.spines['left'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
#plt.xlabel('$x$')
#plt.ylabel('$y$')
plt.grid() # minor
plt.axis('equal')


plt.show()
