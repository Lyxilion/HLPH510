# Nom : BOUCHER
# Prenom : Rubens
# Exercice 2d

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

nbt = 10000  # On augmente le temps de simulation
n_indice = 2.3

# Definition des parametres
c = 2.99792458e8
lambda0 = 1.55e-6
N_lambda = 12
S = 0.6

dx = lambda0 / N_lambda
T = lambda0 / c

nbx = int(20 * lambda0 / dx) + 1  # On augmente le domaine de simulation

dt = S * dx / c

unm = np.zeros(nbx)
un = np.zeros(nbx)
unp = np.zeros(nbx)

eps_r = np.ones(nbx)

xmin = 0
xmax = xmin + dx * (nbx - 1)
x = np.linspace(xmin, xmax, nbx)

# On change l'indice quandon ets dans le milieu
for j in range(nbx):
    if 5 * lambda0 < x[j] < 13.3 * lambda0:
        eps_r[j] = n_indice ** 2
    else:
        eps_r[j] = 1

fig = plt.figure()  # initialise la figure
line1, = plt.plot([], [], label="Ez")
line2, = plt.plot([], [], label="eps_r")
plt.legend()

plt.xlim(xmin, xmax)
plt.ylim(-3, 6)


# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2,


def animate(n):
    tnp = (n + 1) * dt
    unp[0] = np.cos(2 * np.pi / T * tnp) * np.exp(-((tnp - 3.2 * T) / 0.8 * T) ** 2)
    for i in range(1, nbx - 1):
        unp[i] = S ** 2 / eps_r[i] * (un[i - 1] - 2 * un[i] + un[i + 1]) + 2 * un[i] - unm[i]
    line1.set_data(x, unp)
    line2.set_data(x, eps_r)
    unm[:] = un[:]
    un[:] = unp[:]
    return line1, line2,


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=nbt, blit=True, interval=20, repeat=False)
plt.show()
