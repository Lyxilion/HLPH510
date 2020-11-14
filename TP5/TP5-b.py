import matplotlib.pyplot as plt
import numpy as np

n = 1000  # Nombre de point a tirer
nc = 0  # Nombre de point dans le cercle
a = 1.25  # Côté du carré

# Affichage des formes :
# Le Carré :
x = np.array([0, a/2, a/2])
y = np.array([a/2, a/2, 0])
plt.plot(x, y)

# Le Cercle :
theta = np.linspace(0, np.pi/2, 40)
x = a / 2 * np.cos(theta)
y = a / 2 * np.sin(theta)
plt.plot(x, y)

plt.title("Visualisation des points")
plt.axis("equal")

for i in range(n):
    # On tire deux nombres aleatoires, un pour x, un pour y entre -a/2 et a/2
    coords = np.random.uniform(0, a / 2, 2)
    # On verifie si la distance entre le point et l'origine et inferieure au rayon du cercle
    if np.sqrt(coords[0] ** 2 + coords[1] ** 2) <= a / 2:
        nc += 1  # Si il est dans le cercle, on augmente nc
        plt.scatter(coords[0], coords[1], marker=".", c='green')  # si il est dans le cercle => vert
    else:
        plt.scatter(coords[0], coords[1], marker=".", c='red')  # si il est aps dans le cercle rouge

    if i % 100 == 99:  # On rafraichi l'animation que tout les 100 points
        pi_aprox = nc / i * 4  # Calcule de Pi
        print("Aproximation après {} iterations : {}".format(i+1, pi_aprox))
        plt.pause(0.01)

print("Nombre de points total : ", n)
print("Nombre de points dans le cercle : ", nc)
plt.show()  # Garder la figure affiché
