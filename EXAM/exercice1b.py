# Nom : BOUCHER
# Prenom : Rubens
# Exercice 1b

import numpy as np
import matplotlib.pyplot as plt

# Définition des axes
x = np.linspace(-np.pi, np.pi, 149)
y = np.linspace(-2*np.pi, 2*np.pi, 149)

# Decalage des x et y pour eviter erreur lors de la division par 0
x = x + np.finfo(float).eps
y = y + np.finfo(float).eps

X, Y = np.meshgrid(x, y)

Z = (np.sin(2*X)*np.sin(Y)/(2*X*Y)) * np.log(1+X**2+Y**2)  # Calcule de z

# Affichage
plt.pcolormesh(X, Y, Z, shading='auto')
plt.rcParams.update({'mathtext.default': 'regular'})  # Activer la syntax LateX
plt.colorbar().set_label("$f(x,y) = \dfrac{sin(2x)sin(y)}{2xy} ln(1 + x^2 + y^2 )$")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Représentation fonction à deux variables")

plt.show()
