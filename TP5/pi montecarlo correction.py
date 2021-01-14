import numpy as np
import matplotlib.pyplot as plt

n = 0
nc = 0

# definition des points du cercle
theta = np.linspace(0,2*np.pi,40)
xc = 0.5*np.cos(theta)
yc = 0.5*np.sin(theta)

# dessin du cercle
plt.plot(xc,yc)
plt.axis("equal")

for i in range(50000):
    # tirage aleatoire d'un point
    x = np.random.random()-0.5
    y = np.random.random()-0.5
    # incrementation du nombre de points
    n = n + 1
    # determination de l'appartenance au disque
    # affichage en rouge si le point appartient au
    # disque et en bleu sinon
    if np.sqrt(x**2+y**2) < 0.5:
        nc = nc + 1
        plt.plot(x,y,"r,")
    else:
        plt.plot(x,y,"b,")

    # affichage avec une limitation du nombre d'affichages
    if i % 1000 == 0:
        plt.pause(0.01) # pause avec duree en secondes
        # affichage de l'estimation de pi
        print("n = ", n, "approximation de pi", 4*nc/n)

plt.show()