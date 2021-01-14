# Nom : BOUCHER
# Prenom : Rubens
# Exercice 3

import numpy as np
import matplotlib.pyplot as plt

nb_corpuscules = 5
nb_pas = 1000

# on choisit arbitrairement la taille du domaine de simulation
xmin = -10
xmax = 10
ymin = -10
ymax = 10

# on positionne les corpuscules en [0,0]
x = np.zeros(nb_corpuscules)
y = np.zeros(nb_corpuscules)

# on dessine la boite
Xsquare = [-5, 5, 5, -5, -5]
Ysquare = [-5, -5, 5, 5, -5]
plt.plot(Xsquare, Ysquare)

# dessin des corpuscules
line, = plt.plot(x, y, 'o')
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.axis("equal")
# on fixe arbitrairement la taille d'un pas
pas = 0.5

for j in range(nb_pas):
    # deplacement des corpuscules
    for i in range(nb_corpuscules):
        # tirage aleatoire d'un angle de déplacement
        tetha = np.random.random()*2*np.pi
        # calcul des nouvelles coordonnees du corpuscule
        x[i] = x[i] + pas * np.cos(tetha)
        y[i] = y[i] + pas * np.sin(tetha)

        # Verification de sortie de la boite
        if x[i] > 5:
            x[i] = -5
        elif x[i] < -5:
            x[i] = 5
        if y[i] > 5:
            y[i] = -5
        elif y[i] < -5:
            y[i] = 5

    # affichage des nouvelles positions des corpuscules
    line.set_data(x, y)
    plt.pause(0.01)  # pause

plt.show()
