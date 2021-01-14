import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

xdata = []
ydata = []

n = 0
nc = 0

# definition des points du cercle
theta = np.linspace(0, 2 * np.pi, 40)
xc = 0.5 * np.cos(theta)
yc = 0.5 * np.sin(theta)

fig = plt.figure()  # initialise la figure
line1, = plt.plot([], [], ",")
line2, = plt.plot(xc, yc)
plt.axis("equal")


# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line1.set_data([], [])
    line2.set_data(xc, yc)
    return line1, line2,


def animate(i):
    global xdata
    global ydata
    global n
    global nc
    for j in range(500):
        # tirage aleatoire d'un point
        x = np.random.random() - 0.5
        y = np.random.random() - 0.5
        # incrementation du nombre de points
        n = n + 1
        # determination de l'appartenance au disque
        if np.sqrt(x ** 2 + y ** 2) < 0.5:
            nc = nc + 1
        xdata.append(x)
        ydata.append(y)
    line1.set_data(xdata, ydata)
    print("n = ", n, "approximation de pi", 4 * nc / n)
    return line1, line2,


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=500, blit=True, interval=20, repeat=False)

plt.show()