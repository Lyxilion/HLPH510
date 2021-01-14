import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

nbt = 1000
n_indice = 1.45         #CHANGER ICI

c = 2.99792458e8
lambda0 = 1.55e-6       #CHANGER ICI
N_lambda = 20           #CHANGER ICI
S = 0.9                 #CHANGER ICI

dx = lambda0 / N_lambda
T = lambda0 / c

nbx = int(10 * lambda0 / dx) + 1    #CHANGER ICI

dt = S * dx / c

unm = np.zeros(nbx)
un = np.zeros(nbx)
unp = np.zeros(nbx)

eps_r = np.ones(nbx)

xmin = 0
xmax = xmin + dx * (nbx - 1)
x = np.linspace(xmin, xmax, nbx)

for i in range(nbx):
    if x[i] > 5 * lambda0 and x[i] < 7 * lambda0:
        eps_r[i] = n_indice ** 2
    else:
        eps_r[i] = 1

fig = plt.figure()  # initialise la figure
line1, = plt.plot([], [], label="Ez")
line2, = plt.plot([], [], label="eps_r")
plt.legend()

plt.xlim(xmin, xmax)
plt.ylim(-3, 3)


# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2,


t0 = 3 * T
tau = T


def animate(n):
    tnp = (n + 1) * dt
    unp[0] = np.cos(2 * np.pi / T * tnp) * np.exp(-((tnp - t0) / tau) ** 2)         #CHANGER ICI
    for i in range(1, nbx - 1):
        unp[i] = S ** 2 / eps_r[i] * (un[i - 1] - 2 * un[i] + un[i + 1]) + 2 * un[i] - unm[i]

    line1.set_data(x, unp)
    line2.set_data(x, eps_r)

    unm[:] = un[:]
    un[:] = unp[:]

    return line1, line2,


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=nbt, blit=True, interval=20, repeat=False)

plt.show()