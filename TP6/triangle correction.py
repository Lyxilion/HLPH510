import numpy as np
import matplotlib.pyplot as plt

# definition des sommets du triangle
x = np.array([-.5, 0, .5, -.5])
y = np.array([0, np.sqrt(3) / 2., 0, 0])

# dessin du triangle
plt.plot(x, y)
plt.axis('equal')

# choix d'un point de depart arbitraire
x0 = 0.3
y0 = 0.1
plt.plot(x0, y0, 'b,')

for i in range(20000):
    # tirage aleatoire d'un des sommets
    n = int(np.random.random() * 3)
    # calcul des coordonnees du nouveau point
    x0 = (x0 + x[n]) / 2
    y0 = (y0 + y[n]) / 2
    plt.plot(x0, y0, 'b,')
    # affichage avec une limitation du nombre d'affichages
    if i % 1000 == 0:
        plt.pause(0.01)  # pause avec duree en secondes

plt.show()