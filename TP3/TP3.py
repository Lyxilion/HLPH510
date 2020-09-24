import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)

def random_walk():
    """

    :return:
    """
    x = np.array([[0],[0]])
    for i in range(9) :
        if np.random.random() < 0.5 :
            x = np.append(x,np.array([[i+1],[x[1,i]+1]]),axis = 1)
        else :
            x = np.append(x,np.array([[i+1],[x[1,i]-1]]),axis = 1)
    return x

x = random_walk()
plt.plot(x[0],x[1])
plt.plot(x[0],x[1]**2)

#plt.show()

data = np.linspace(0,9,10)
for i in range(3):
    data = np.vstack((data,random_walk()[1]))
print(data)