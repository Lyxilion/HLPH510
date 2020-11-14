import matplotlib.pyplot as plt
import numpy as np

# On igniore l'erreur de lors de la division par 0
np.seterr(divide='ignore', invalid='ignore')

# Deffinition de la fonction
f = lambda x : np.sin(x) * np.sqrt(x**2 + 1) / x

# Calcule des coordonnées
x= np.linspace(-6,6,121)
y = f(x)

# Affichage de la courbe
plt.plot(x,y)
plt.show()