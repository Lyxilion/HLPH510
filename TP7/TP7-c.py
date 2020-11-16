import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 101)
z = 5*np.exp(-2j*x*np.pi)*np.exp(-x**2)

X = np.array([x, x])

y0 = np.zeros(len(x))
y = np.abs(z)
Y = np.array([y0, y])

Z = np.array([z, z])
C = np.angle(Z)

# Affichages des informations du graph
plt.rcParams.update({'mathtext.default': 'regular'})  # Activer la syntax LateX
plt.title("$y = e^{-i2 \pi x}  e^{-x^{2}}$")
plt.xlabel("x")
plt.ylabel("Module de y")

# Affichage du module
plt.plot(x, y, "k")

# Affichage de l'argument
plt.pcolormesh(X, Y, C, shading="gouraud", cmap=plt.cm.hsv, vmin=-np.pi, vmax=np.pi)
plt.colorbar().set_label("Argument de y")

plt.show()
