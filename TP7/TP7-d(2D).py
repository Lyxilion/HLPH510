import numpy as np
import matplotlib.pyplot as plt

# Définition des axes
x = np.linspace(-2, 2, 21)      #CHANGER ICI
y = np.linspace(-7, 7, 29)      #CHANGER ICI
X, Y = np.meshgrid(x, y)

Z = np.log(3*X**2+Y**2+1)  # Calcule de z   #CHANGER ICI

# Affichage
plt.pcolormesh(X, Y, Z, shading='auto')
plt.rcParams.update({'mathtext.default': 'regular'})  # Activer la syntax LateX
plt.colorbar().set_label("$f(x,y) = ln(3x^2 + y^2 + 1)$")       #CHANGER ICI
plt.xlabel("x")
plt.ylabel("y")
plt.title("Représentation fonction à deux variables")

plt.show()
