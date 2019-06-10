import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
from scipy import signal
from scipy import misc
from skimage import data
from skimage import transform

imsrc = Image.open('pepper_salt_graph.jpg').convert('L')
ax = plt.imshow(imsrc, cmap='gray')
plt.show()

# median filter
print(imsrc)
imout = signal.medfilt2d(imsrc, 3)
plt.imshow(imout, cmap='gray')
plt.show()

# detailed image format conversion, see https://www.jianshu.com/p/bdd9bfcbedb7