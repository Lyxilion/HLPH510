import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

x = np.linspace(-3, 13, 161)
dt = 0.1

fig = plt.figure()  # initialise la figure
line, = plt.plot([], [])
plt.xlim(-3, 13)
plt.ylim(-1, 1.5)


def animate(i):
    t = i * dt
    y = 1 / (1 + (x - 4.8*t)**2)
    line.set_data(x, y)
    return line,


ani = animation.FuncAnimation(fig, animate,  frames=41, interval=20, repeat=False)
plt.show()
