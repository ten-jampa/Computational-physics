import numpy as np
from vpython import vector, sphere, arrow, rate, color

## A moving sphere
# pi = np.pi
# pos = vector(1,0,0)
# r = 0.1
# s = sphere(pos = pos, radius = r)
# for theta in np.arange(0, 10*pi, 0.1):
#     rate(30) #tells the computer to wait 1/x of a second from the time you call rate before each change you make on the screen
#     # without the rate function, changes will appear discrete and too fast to be even smooth
#     x = np.cos(theta)
#     y = np.sin(theta)
#     s.pos = vector(x, y, 0)


## Exercise 3.5: Visualization of the solar system

#radius in km
c1 = 1000 #scale factor for radii
c2 = 1000 #scale factor for time
sun = sphere( pos = vector(0,0,0), radius = 6.9e5, color = color.yellow, make_trail = True)
mercury = sphere(pos = vector(57.9e6, 0,0), radius = 2.4e3*c1, color = color.orange, make_trail = True )
venus = sphere(pos = vector(108.2e6, 0, 0), radius = 6.1e3*c1, color = color.white, make_trail = True)
earth = sphere(pos = vector(149.6e6, 0, 0), radius = 6.3e3*c1, color = color.blue, make_trail = True)
mars = sphere(pos = vector(227.6e6, 0, 0), radius = 3.38e3*c1, color = color.red, make_trail = True)

#period of orbit(in days)
T_mer = 88
T_Ven = 224.7
T_earth = 365.3
T_mars = 687.0


solar_system = np.array([sun, mercury, venus, earth, mars])

# a planetary motion
for time in np.arange(0, 10*T_earth, 10):
    rate(20)
    dtheta = T_earth*time
    earth.pos = vector(earth.pos.x*np.cos(dtheta), earth.pos.y*np.sin(dtheta), 0)