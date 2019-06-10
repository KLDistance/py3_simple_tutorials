import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')

# load data
imsrc = pd.read_csv('Normal_ITO.csv', header=None)
X_vec = np.linspace(0, 1.50, np.shape(imsrc)[1])
Y_vec = np.linspace(0, 1.65, np.shape(imsrc)[0])
X, Y = np.meshgrid(X_vec, Y_vec)
print(np.shape(imsrc))
surf = ax.plot_surface(X, Y, imsrc, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(14000, 17000)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()