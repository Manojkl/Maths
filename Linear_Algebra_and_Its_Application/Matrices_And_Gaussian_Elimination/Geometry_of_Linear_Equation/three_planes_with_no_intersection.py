import numpy as np
import matplotlib.pyplot as plt

# Define the equation of the plane
# aX+bY+cZ+d = 0
a, b, c, d = 1, 1, 1, -2

# Create a grid of points for the x, y coordinates
x, y = np.linspace(-20, 20, 100), np.linspace(-20, 20, 100)
X, Y = np.meshgrid(x, y)

# Calculate the corresponding z value for each point on the grid
Z = (-d - a*X - b*Y)/c

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='y')

a, b, c, d = 2, 0, 3, -5

Z = (-d - a*X - b*Y)/c
Z = 0 

x = np.linspace(-20, 20, 100)
y = (2*x-5)/3
ax.plot(x, y, '-r')

# ax.plot_surface(X, Y, Z, color='m')

a, b, c, d = 3, 1, 4, -7

Z = (-d - a*X - b*Y)/c

ax.plot_surface(X, Y, Z, color='m')

# a, b, c, d = 2, 0, 3, 5

# Z = (-d - a*X - b*Y)/c

# ax.plot_surface(X, Y, Z, color='c')

plt.show()
