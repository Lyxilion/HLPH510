import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Calcule des Coordonnées
x = np.linspace(-3, 13, 161)
dt = 0.1

fig = plt.figure()  # initialise la figure
line, = plt.plot([], [])
plt.xlim(-3, 13)
plt.ylim(-1, 1.5)


def animate(i):
    t = i * dt
    y = 1 / (1 + (x - 4.8*t)**2)  # Expression de la fonction
    line.set_data(x, y)
    return line,

# Animation
ani = animation.FuncAnimation(fig, animate,  frames=41, interval=20, repeat=False)
plt.show()
