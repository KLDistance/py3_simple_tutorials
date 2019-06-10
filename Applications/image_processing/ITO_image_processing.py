# the Normal_ITO sample is the Indium-tin oxide prepared by Hewlett Packard Enterprise
# the image is obtained using self-developed Scanning-ion Conductance Microscopy by Yunong Wang
# on Nov 12nd, 2017, in SUSTech, China

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import signal
from scipy import misc
from skimage import data
from skimage import transform
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# eliminate the slope in the image
def Slope_Diminish(imsrc, orientation) : 
    src_row, src_col = np.shape(imsrc)
    imtmp = imsrc
    # wipe out slope in x direction
    if 'x' in orientation : 
        x_zvec = np.linspace(imtmp[0][0], imtmp[0][src_col - 1], src_col) - imtmp[0][0]
        imtmp = imtmp - x_zvec
    if 'y' in orientation : 
        y_zvec = np.linspace(imtmp[0][0], imtmp[src_row - 1][0], src_row) - imtmp[0][0]
        imtmp = (imtmp.T - y_zvec).T
    return imtmp

# eliminate the bending curve effect (deprecated)
def Surface_Bend_1d_Ref(imsrc, ref_line_index, base_height, fit_num, orientation) : 
    src_row, src_col = np.shape(imsrc)
    x_coord = np.arange(0, src_col)
    y_coord = np.arange(0, src_row)
    imtmp = imsrc
    if 'x' in orientation : 
        polyfit_coeff = np.polyfit(x_coord, imtmp[ref_line_index, :], fit_num)
        ref_map = np.polyval(polyfit_coeff, x_coord)
        imtmp = imtmp - ref_map + base_height
    if 'y' in orientation : 
        polyfit_coeff = np.polyfit(y_coord, imtmp[:, ref_line_index], fit_num)
        ref_map = np.polyval(polyfit_coeff, y_coord)
        imtmp = (imtmp.T - ref_map + base_height).T
    return imtmp

# using low-pass to eliminate bending effect
def Surface_Bend_Lp(imsrc, ref_line_index, base_height, fc, orientation) : 
    src_row, src_col = np.shape(imsrc)
    imtmp = imsrc
    if 'x' in orientation : 
        b, a = signal.butter(1, fc, btype='lowpass')
        baseline = signal.lfilter(b, a, imtmp[ref_line_index, :])
        imtmp = imtmp - baseline
    if 'y' in orientation : 
        b, a = signal.butter(1, fc, btype='lowpass')
        baseline = signal.lfilter(b, a, imtmp[:, ref_line_index])
        print(np.shape(imtmp[ref_line_index, :]))
        imtmp = (imtmp.T - baseline).T
    return imtmp + base_height

# eliminate salt-and-pepper noise
def Surface_Medfilt(imsrc) : 
    src_row, src_col = np.shape(imsrc)
    # apply 2D medfilt to process central bodies with a 3x3 filter (inline a transpose)
    imtmp = signal.medfilt2d(imsrc, 3)
    # apply 1D medfilt to process boundaries
    imtmp[0, :] = imtmp[1, :]
    imtmp[src_row - 1, :] = imtmp[src_row - 2, :]
    imtmp[:, 0] = imtmp[:, 1]
    imtmp[:, src_col - 1] = imtmp[:, src_col - 2]
    # cancel side effects at corners
    imtmp[0, 0] = imtmp[1, 0]
    imtmp[0, src_col - 1] = imtmp[0, src_col - 2]
    imtmp[src_row - 1, 0] = imtmp[src_row - 2, 0]
    imtmp[src_row - 1, src_col - 1] = imtmp[src_row - 2, src_col - 2]
    return imtmp

# interpolate the image
def Surface_Interpolate(imsrc, stretched_row, stretched_col) : 
    return transform.resize(imsrc, (stretched_row, stretched_col), order=1)

# display 3D plot
def Surface_3D_Display(imsrc, act_width, act_height) :
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    row_num, col_num = np.shape(imsrc)
    X_vec = np.linspace(0, act_width, col_num)
    Y_vec = np.linspace(0, act_height, row_num)
    X, Y = np.meshgrid(X_vec, Y_vec)
    surf = ax.plot_surface(X, Y, imsrc, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

if __name__ == '__main__' : 
    # load the image (beware the header is None!)
    imsrcpd = pd.read_csv('Normal_ITO.csv', header=None)
    imsrc = imsrcpd.values + 0.0
    row, col = np.shape(imsrc)
    # bending diminish (using low-pass validation instead of polyfit!)
    #im_curve_diminish = Surface_Bend_1d_Ref(imsrc, 10, 2000, 4, 'x')
    #im_curve_diminish = Surface_Bend_Lp(imsrc, 0, 4000, 0.05, 'xy')[np.arange(25, row), :]
    #im_curve_diminish = im_curve_diminish[:, np.arange(25, col)]
    # slope diminish
    im_slope_diminish = Slope_Diminish(imsrc, 'y')
    # median filter
    im_medfilt = Surface_Medfilt(im_slope_diminish)
    # interpolate the image
    imout = Surface_Interpolate(im_medfilt, 800, 800)
    # display the image
    Surface_3D_Display(imsrc, 1.65, 1.5)

    # detailed types of noise see https://blog.csdn.net/weixin_40446557/article/details/81451651