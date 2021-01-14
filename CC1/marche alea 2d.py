import numpy as np
import matplotlib.pyplot as plt

nb_corpuscules = 10
nb_pas = 1000

# on choisit arbitrairement la taille du domaine de simulation
xmin = 0
xmax = 20
ymin = 0
ymax = 15

# on positionne les corpuscules au hasard
x = xmin + (xmax - xmin) * np.random.random(nb_corpuscules)
y = ymin + (ymax - ymin) * np.random.random(nb_corpuscules)

# dessin des corpuscules
line, = plt.plot(x, y, 'bo')
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

# on fixe arbitrairement la taille d'un pas
pas = 0.1

# definition des coordonnees des pas pour les 4 differentes directions
# haut, bas, gauche, droite
x_pas = np.array([0, 0, -pas, pas])
y_pas = np.array([pas, -pas, 0, 0])

for i in range(nb_pas):
    # deplacement des corpuscules
    for corpuscule in range(nb_corpuscules):
        # tirage aleatoire d'une des 4 directions
        n = int(4 * np.random.random())
        # calcul des nouvelles coordonnees du corpuscule
        x[corpuscule] = x[corpuscule] + x_pas[n]
        y[corpuscule] = y[corpuscule] + y_pas[n]

    # affichage des nouvelles positions des corpuscules
    line.set_data(x, y)
    plt.pause(0.01)  # pause avec duree en secondes

plt.show()
