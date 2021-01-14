# Nom : BOUCHER
# Prenom : Rubens
# Exercice 2c

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

nbt = 1000

c = 2.99792458e8
lambda0 = 1.55e-6
N_lambda = 12
S = 0.1     # S plus petit

dx = lambda0 / N_lambda
T = lambda0 / c

nbx = int(14 * lambda0 / dx) + 1

dt = S * dx / c

unm = np.zeros(nbx)
un = np.zeros(nbx)
unp = np.zeros(nbx)

xmin = 0
xmax = xmin + dx * (nbx - 1)
x = np.linspace(xmin, xmax, nbx)

fig = plt.figure()  # initialise la figure
line, = plt.plot([], [])

plt.xlim(xmin, xmax)
plt.ylim(-3, 3)


def init():
    line.set_data([], [])
    return line,


def animate(n):
    tnp = (n + 1) * dt
    unp[0] = np.cos(2*np.pi/T*tnp) * np.exp(-((tnp-3.2*T)/0.8*T)**2)
    for i in range(1, nbx - 1):
        unp[i] = S ** 2 * (un[i - 1] - 2 * un[i] + un[i + 1]) + 2 * un[i] - unm[i]
    line.set_data(x, unp)
    unm[:] = un[:]
    un[:] = unp[:]
    return line,


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=nbt, blit=True, interval=20, repeat=False)
plt.show()
