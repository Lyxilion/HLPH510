import numpy as np
import matplotlib.pyplot as plt

# on definit un epsilon
epsilon = np.finfo(float).eps

x = np.linspace(-10, 10, 101)

# on ajoute epsilon pour eviter la division par zero
x = x + epsilon

z = np.sin(x)/x*np.exp(-1j*np.pi*x)

X = np.array([x,x])

y0 = np.zeros(len(x))
y = np.abs(z)
Y = np.array([y0,y])

Z = np.array([z,z])
C = np.angle(Z)

plt.plot(x, y, "k")

plt.pcolormesh(X, Y, C, shading="gouraud", cmap=plt.cm.hsv, vmin=-np.pi, vmax=np.pi)
plt.colorbar()

plt.show()