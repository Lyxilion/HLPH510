import numpy as np
import matplotlib.pyplot as plt

xmin = -1
xmax = 1
dx = 0.1
nbx = int( (xmax-xmin)/dx ) + 1
ymin = -3
ymax = 3
dy = 0.3
nby = int( (ymax-ymin)/dy ) + 1

x = np.linspace(xmin, xmax, nbx)
y = np.linspace(ymin, ymax, nby)
X, Y = np.meshgrid(x, y)

Z = np.sin(Y)*np.exp(-X**2) # calcul du tableau des valeurs de Z

plt.imshow(Z, interpolation="bicubic",
           origin="lower", extent=[xmin,xmax,ymin,ymax])
plt.colorbar()

plt.show()