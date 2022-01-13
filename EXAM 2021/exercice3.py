# Nom : BOUCHER
# Prenom : rubens
# Exercice 3

import matplotlib.pyplot as plt
import numpy as np

Px = np.random.uniform(0, 10, 8)
Py = np.random.uniform(0, 10, 8)


for i in range(50) :
    for i in range(len(Px)):
        rnd = np.random.randint(0, 4)  # Tirage d'un entier aléatoire entre 1 et 4
        if rnd == 0 :
            Py[i] += 0.5
        elif rnd == 1 :
            Px[i] += 0.5
        elif rnd == 2 :
            Py[i] -= 0.5
        elif rnd == 3 :
            Px[i] -= 0.5

        plt.scatter(Px[i], Py[i])
    plt.pause(0.01)

    plt.clf()
    plt.xlim(0, 10)
    plt.ylim(0, 10)
plt.show()