## To learn visual python for 3-d graphics
from vpython import sphere, vector, color, box, cylinder, arrow, cone, pyramid
import numpy as np
from numpy import array

'''Creating a Sphere lattice in a box of length L
L = 5 # length of the box
R = 0.3 # radius of a single molecule

for x in range(-L, L+1):
	for y in range(-L, L+1):
		for z in range(-L, L+1):
			pos = vector(x,y,z)
			sphere(pos = pos, radius = R)
box(pos = vector(0,0,0), length =2, height = 1, width =1, color= color.green)
'''
## Exercise 3.2

'''a) A sodium chloride crystal has sodium and chlorine atoms arranged 
on a cubic lattice but the atoms alternate between sodium and chlorine,
so that each sodium is surrounded by six chlorines and 
each chlorine is surrounded by six sodiums. Create a visualization of the sodium chloride lattice using 
two different colors to represent the two types of atoms
'''

# L = 5
# R = 0.3
# for x in range(-L, L+1):
#     for y in range(-L, L+1):
#         for z in range(-L, L+ 1):
#             pos = vector(x,y,z)
#             if (x+y+z)%2 == 0: # any one increment always switches from odd to even to odd
#                 sphere(pos = pos, radius = R, color = color.white) # White is sodium
#             else:
#                 sphere(pos = pos, radius = R, color = color.blue) #blue is chlorine

'''b) Theface-centeredcubic (FCC)lattice,which isthemost
common lattice in naturally occurring crystals, consists of a cubic lattice with atoms position not 
only at the corners of each cube but also at the center of each face. Create a visualisation
of an fcc latticewith a single species of atom'''

# L = 5 
# R = 0.1
# steps = np.arange(0, 1.1, 0.5)
# for x in steps:
#     for y in steps:
#         for z in steps:
#             pos = vector(x, y, z)
#             if (x + y + z)%1 == 0:
#                     sphere(pos = pos, radius = R)
            

# pos = vector(0,0,0)
# s = sphere()
# s.color = color.blue
# s.radius = 2
# a = arrow()
# a.color = color.red

s = np.empty(10, sphere)
for n in range(10):
    s[n] = sphere()

print(s)

pos_vec = vector(1,1,1)
axis_1 = vector(1,2,1)
size = vector(3, 2, 1)
R = 1
L = 1.5
H = 2.
W = 0.5

box(pos=[x,y,z], axis=[a,b,c],length=L, height=H, width=W, up=[q,r,s])
cone(pos=[x,y,z], axis=[a,b,c], radius=R)
cylinder(pos=[x,y,z], axis=[a,b,c], radius=R) 
pyramid(pos=[x,y,z], size=[z,b,c]) 
arrow(pos=[x,y,z], axis=[a,b,c], headwidth=H, headlength=L, shaftwidth=W)