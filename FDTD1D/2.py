import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

c = 1
S = 1
dx = 0.1
nbx = 100

xmin = 0
xmax = xmin + (nbx - 1) * dx

dt = S * dx / c
nbt = 500

x = np.linspace(xmin, xmax, nbx)

unm = np.zeros(nbx)
un = np.zeros(nbx)
unp = np.zeros(nbx)

fig = plt.figure()  # initialise la figure
line, = plt.plot([], [])
plt.xlim(xmin, xmax)
plt.ylim(-1.5, 1.5)


# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([], [])
    return line,


t0 = 30 * dt
tau = 10 * dt


def animate(n):
    tnp = (n + 1) * dt
    unp[0] = np.exp(-((tnp - t0) / tau) ** 2)
    for i in range(1, nbx - 1):
        unp[i] = S ** 2 * (un[i + 1] - 2 * un[i] + un[i - 1]) + 2 * un[i] - unm[i]
    line.set_data(x, unp)
    unm[:] = un[:]
    un[:] = unp[:]
    return line,


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=nbt, blit=True, interval=20, repeat=False)

plt.show()