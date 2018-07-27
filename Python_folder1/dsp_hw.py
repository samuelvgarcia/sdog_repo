import numpy as np; r_, pi = np.r_, np.pi
from numpy.fft import fft, ifft, fftshift
import matplotlib.pyplot as plt
# plt.ion()
plt.close('all')

n = r_[0:64]
f0 = 100
f1 = 150
fs = 310

x = 5*np.cos(2*pi*f0/fs*n + 2*pi/12) + 4*np.sin(2*pi*f1/fs * n)

plt.plot( n, x)
plt.grid(1)

X = fft(x)
plt.figure(2)
plt.plot(np.abs(X)), plt.grid(1)

M = 256
a = M*x.size
b = int(x.size /2)
##
X_zp = r_[X[:b], 1j*np.zeros(a), X[b:]]


##
x_int = ifft((X_zp))

plt.figure(3)
plt.plot(M*np.real(x_int[:3000])), plt.grid(1)


##
n = r_[0:100]
f0 = 100
f1 = 150
fs = 3000

x2 = 5*np.cos(2*pi*f0/fs*n + 2*pi/12) + 4*np.sin(2*pi*f1/fs * n)
plt.figure(4)
plt.plot(x2), plt.grid(1)
plt.show()