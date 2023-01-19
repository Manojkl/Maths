from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, 0, 0, 9, arrow_length_ratio=0.3)
ax.quiver(0, 0, 0, 5, 0, 0, arrow_length_ratio=0.3)
ax.quiver(0, 0, 0, 0, -2, 0, arrow_length_ratio=0.3)
ax.quiver(0, 0, 0, 5, -2, 9, arrow_length_ratio=0.3)

ax.quiver(0, 0, 0, 2, 0, 4, arrow_length_ratio=0.3)
ax.quiver(0, 0, 0, 3, -2, 5, arrow_length_ratio=0.3)
ax.quiver(2, 0, 4, 5, -2, 9, linestyle='--')

# ax.quiver(5, 0, 9, 5, 0, 0, linestyle='--')
# ax.quiver(5, 0, 9, 0, 0, 9, linestyle='--')
# ax.quiver(5, 0, 9, 5, -2, 9, linestyle='--')
# ax.quiver(5, -2, 9, 0, -2, 9, linestyle='--')
# ax.quiver(5, -2, 9, 5, -2, 0, linestyle='--')
# ax.quiver(5, 0, 0, 5, -2, 0, linestyle='--')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
plt.show()