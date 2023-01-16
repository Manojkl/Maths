import numpy as np
import matplotlib.pyplot as plt

# Define the equation of the plane
a, b, c, d = 2, 1, 1, -5

# Create a grid of points for the x, y coordinates
x, y = np.linspace(-20, 20, 100), np.linspace(-20, 20, 100)
X, Y = np.meshgrid(x, y)

# Calculate the corresponding z value for each point on the grid
Z = (-d - a*X - b*Y)/c

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='y')

a, b, c, d = 4, -6, 0, -2

Z = (-d - a*X - b*Y)/c

ax.plot_surface(X, Y, Z, color='m')

a, b, c, d = -2, 7, 2, -9

Z = (-d - a*X - b*Y)/c

ax.plot_surface(X, Y, Z, color='m')

plt.show()
