import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import math

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(0, 1600, 1)
Y = np.arange(0, 1600, 1)
X, Y = np.meshgrid(X, Y)
def f(x,y):
    return ( 5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) ) * math.e**( -abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7) )
R = 1
Z = f(X,Y)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0, 50000)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

print(f(200,200),f(1400,1400))