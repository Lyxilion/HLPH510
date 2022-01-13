# Nom : BOUCHER
# Prenom : rubens
# Exercice 1a

import matplotlib.pyplot as plt
import numpy as np

# Définition des axes
x = np.linspace(-2, 2, 21)
y = np.linspace(-3, 3, 21)
y = y + np.finfo(float).eps
X, Y = np.meshgrid(x, y)

Z = np.sin(Y)*np.exp(-X**2)  # Calcule de z

# Affichage
plt.pcolormesh(X, Y, Z, shading='auto')
plt.rcParams.update({'mathtext.default': 'regular'})  # Activer la syntax LateX
plt.colorbar().set_label("$f(x,y) = sin(y)e^{-x^2}$")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Représentation fonction à deux variables")

plt.show()
