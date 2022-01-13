# Nom : BOUCHER
# Prenom : rubens
# Exercice 1b

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-9, 9, 91)
x = x + np.finfo(float).eps

z = (np.sin(x) / x ) * np.exp(-1j*np.pi*x)

X = np.array([x, x])

y0 = np.zeros(len(x))
y = np.abs(z)
Y = np.array([y0, y])

Z = np.array([z, z])
C = np.angle(Z)

# Affichages des informations du graph
plt.rcParams.update({'mathtext.default': 'regular'})  # Activer la syntax LateX
plt.title("$y = sin(x)/x * e^{-ix\pi}$")
plt.xlabel("x")
plt.ylabel("Module de y")

# Affichage du module
plt.plot(x, y, "k")

# Affichage de l'argument
plt.pcolormesh(X, Y, C, shading="gouraud", cmap=plt.cm.hsv, vmin=-np.pi, vmax=np.pi)
plt.colorbar().set_label("Argument de y")

plt.show()
