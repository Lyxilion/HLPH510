import matplotlib.pyplot as plt
import numpy as np
np.random.seed(9)

n = 1000                   #Nombre de point a tirer
nc = 0                      #Nombre de point dans le cercle

a = 1.25                      #cote du carre

#carre
x = np.array([-a/2, a/2, a/2, -a/2, -a/2])
y = np.array([a/2, a/2, -a/2, -a/2, a/2])
plt.plot(x, y)

#cercle
theta = np.linspace(0, 2*np.pi, 40)
x = a / 2 * np.cos(theta)
y = a / 2 * np.sin(theta)
plt.plot(x, y)
plt.axis("equal")
plt.xlim(-a, a)

for i in range(n):
    coords = np.random.uniform(-a/2, a/2, 2)        #On tire deux nombre aleatoir, un pour x, un pour y entre -a/2 et a/2
    if np.sqrt(coords[0]**2+coords[1]**2) <= a/2 :  #On verifie si la distance entre le point et l'origine et inferieure au rayon du cercle
        nc += 1                                     #Si il est dans le cercle, on augmente le nc
        plt.scatter(coords[0],coords[1], c='green') #si il est dans le cercle => vert
    else :
        plt.scatter(coords[0], coords[1], c='red')  #si il est aps dans le cercle rouge
    if i%100==0 :                                   #pour economiser de temps, on affiche tout les 100 point
        plt.pause(0.01)                             #le truc qui refrech l'animation
        pi_aprox = nc / n * 4                       #On a nc/n = pi/4, on obtien donc une aproximation de pi
        print(pi_aprox)
pi_aprox = nc / n * 4
print(pi_aprox)
plt.show()


