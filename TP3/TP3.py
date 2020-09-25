import matplotlib.pyplot as plt
import numpy as np

np.random.seed(9)

def random_walk():
    """
        Fait une marche aleatoire de 100 pas
    :return:
    """
    x = np.array([0])
    for i in range(99) :
        if np.random.random() < 0.5 :
            x = np.append(x,np.array([x[i]+1]))
        else :
            x = np.append(x,np.array([x[i]-1]))
    return x

time = np.linspace(0,100,100)
x = random_walk()

plt.plot(time,x)
plt.title("Marche aleatoir.")
plt.xlabel("Temps")
plt.ylabel("Distance")
plt.show()

plt.plot(time,x**2)
plt.title("Distance au carré.")
plt.xlabel("Temps")
plt.ylabel("Distance")
plt.show()

for i in range(499):
    x = np.vstack((x,random_walk()))

sum = np.sum(x, axis=0)/len(x)

plt.plot(time,sum)
plt.title("Moyenne des 500 marches")
plt.xlabel("Temps")
plt.ylabel("Distance")
plt.show()