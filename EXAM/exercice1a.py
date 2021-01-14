# Nom : BOUCHER
# Prenom : Rubens
# Exercice 1a

import matplotlib.pyplot as plt
import numpy as np

# Deffinition de la fonction
f = lambda k: np.sin(k-1) / (k-1) * np.sqrt(2*k**2 + 3)
# Calcule des coordonnées
x = np.linspace(-8, 10, 91)
# Decalage des x pour eviter erreur lors de la division par 0
x = x + np.finfo(float).eps
y = f(x)

# Affichage de la courbe
plt.rcParams.update({'mathtext.default': 'regular'})  # Activer la syntax LateX
plt.title("$f(x) = \dfrac{sin(x-1)}{x-1} \sqrt{2x^2 + 3}$")
plt.ylabel("y")
plt.xlabel("x")
plt.plot(x, y)
plt.show()
