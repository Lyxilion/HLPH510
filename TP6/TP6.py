import matplotlib.pyplot as plt
import numpy as np

a = 3.5  # Longueur d'un coté du triangle
x = [0, a, a / 2, 0]  # Calcule des coordonnées des sommets
y = [0, 0, np.sqrt(a ** 2 - (a ** 2 / 4)), 0]

x_p = 2  # Coordonnées du point arbitraire P
y_p = 0.5

plt.plot(x, y)  # tracé du triangle et de P
plt.scatter(x_p, y_p, marker="o", c='red')

for i in range(10):
    rnd = np.random.randint(0, 3)  # Tirage d'un entier aléatoire entre 1 et 3
    # Calcule des coordonnées du nouveau point
    x_p = (x_p + x[rnd]) / 2
    y_p = (y_p + y[rnd]) / 2
    plt.scatter(x_p, y_p, marker=".", c='green')  # Tracé du point
    plt.pause(0.01)
plt.show()
