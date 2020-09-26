import matplotlib.pyplot as plt
import numpy as np
np.random.seed(9)


def random_walk():
    """
        Fait une marche aleatoire de 100 pas
    :return:
    """
    walk = np.array([0])
    for i in range(99):
        if np.random.random() < 0.5:
            walk = np.append(walk, np.array([walk[i]+1]))
        else:
            walk = np.append(walk, np.array([walk[i]-1]))
    return x


time = np.linspace(0, 100, 100)
x = random_walk()

plt.plot(time, x)
plt.title("Marche aleatoir.")
plt.xlabel("Temps")
plt.ylabel("Distance")
plt.show()

plt.plot(time, x**2)
plt.title("Distance au carré.")
plt.xlabel("Temps")
plt.ylabel("Distance")
plt.show()

for n in range(499):
    x = np.vstack((x, random_walk()))

moy = np.sum(x, axis=0)/len(x)

plt.plot(time, moy)
plt.title("Moyenne des 500 marches")
plt.xlabel("Temps")
plt.ylabel("Distance")
plt.show()
