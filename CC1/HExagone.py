import numpy as np
import matplotlib.pyplot as plt

ratio = 0.30

# definition des sommets de l'hexagone
x = np.array([1, 0.5, -0.5, -1, -0.5, 0.5, 1])
y = np.array([0, np.sqrt(3) / 2, np.sqrt(3) / 2, 0, -np.sqrt(3) / 2, -np.sqrt(3) / 2, 0])

# dessin de l'hexagone
plt.plot(x, y)
plt.axis('equal')

# choix d'un point de depart arbitraire
x0 = 0.3
y0 = 0.1
plt.plot(x0, y0, 'b,')

for i in range(20000):
    # tirage aleatoire d'un des sommets
    n = int(np.random.random() * 6)
    # calcul des coordonnees du nouveau point
    x0 = ratio * x0 + (1 - ratio) * x[n]
    y0 = ratio * y0 + (1 - ratio) * y[n]
    plt.plot(x0, y0, 'b,')
    # affichage avec une limitation du nombre d'affichages
    if i % 1000 == 0:
        plt.pause(0.01)  # pause avec duree en secondes

plt.show()