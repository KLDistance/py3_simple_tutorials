import numpy as np
from scipy import signal

# generate a 32x32 scaled matrix with random floats 0~1
signal_matrix = np.random.rand(32, 32)
print(signal_matrix)

# 2D fast fourier transform
freq_matrix = np.fft.fft(signal_matrix)
print('frequency domain signal\n', freq_matrix)

# constructed low pass filter and filt the signal
lp_filter = np.matrix([[1/9,1/9,1/9] , [1/9,1/9,1/9] , [1/9,1/9,1/9]])
filt_signal = signal.convolve2d(lp_filter, signal_matrix)
print('lowpass filtering signal\n', filt_signal)