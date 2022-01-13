# Nom : BOUCHER
# Prenom : rubens
# Exercice 2

import matplotlib.pyplot as plt
import numpy as np

a = 1

x1 = 1
y1 = 2

x2 = x1 + np.sqrt(3)/2*a
y2 = y1 - np.sqrt(a**2-(np.sqrt(3)/2*a)**2)

x3 = x2
y3 = y2 - a

x4 = x1
y4 = y3 - np.sqrt(a**2-(np.sqrt(3)/2*a)**2)

x5 = x1 - np.sqrt(3)/2*a
y5 = y3

x6 = x5
y6 = y2

X = [x1, x2, x3, x4, x5, x6, x1]
Y = [y1, y2, y3, y4, y5, y6, y1]

plt.plot(X, Y)
plt.axis("equal")


x_p = 1  # Coordonnées du point arbitraire P
y_p = 1

plt.scatter(x_p, y_p, marker="o", c='red')

for i in range(50):
    rnd = np.random.randint(0, 6)  # Tirage d'un entier aléatoire entre 0 et 5
    # Calcule des coordonnées du nouveau point
    """
    Je n'ai pas réusis a calculer les nouvelle coordonnée
    """

    x_p = (x_p + X[rnd]) * 0.5
    y_p = (y_p + Y[rnd]) * 0.5
    plt.scatter(x_p, y_p, marker=".", c='green')  # Tracé du point
plt.show()


