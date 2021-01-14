import matplotlib.pyplot as plt
import numpy as np

# On igniore l'erreur de lors de la division par 0
np.seterr(divide='ignore', invalid='ignore')

# Deffinition de la fonction
f = lambda k: np.sin(k) * np.sqrt(k**2 + 1) / k         #CHANGER ICI

# Calcule des coordonnées
x = np.linspace(-6, 6, 121)                             #CHANGER ICI
y = f(x)

# Affichage de la courbe
plt.plot(x, y)
plt.show()
