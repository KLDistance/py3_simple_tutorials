import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

imsrc = pd.read_csv('Normal_ITO.csv')
ax = plt.imshow(imsrc, cmap='gray')
plt.show()