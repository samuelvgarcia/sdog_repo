import numpy as np; r_, pi = np.r_, np.pi
import matplotlib.pyplot as plt
plt.ion()
plt.close('all')


## Two sinusoids
n = r_[0:2000]
f1 = 500 #freq1 in kHz
f2 = 496 #freq2 in kHz
fs = 6000 #sampling freq (highly oversampled)

x1 = np.cos(2*pi*f1/fs*n) #signal 1
x2 = np.cos(2*pi*f2/fs*n) #signal 2

# Plot Signals 1 and 2
plt.subplot(211)
plt.plot(x1), plt.plot(x2), plt.grid(1)
plt.xlim([0,250])
plt.title("Two Sinusoids")


## Summation 
x3 = x1 + x2 #Signal 3
x4 = 2*np.cos(2*pi*(f1-f2)/2/fs*n) #Equiv beat frequency envelope

# Plot Combined Signal
plt.subplot(212)
plt.plot(x3), plt.plot(x4,'r', linewidth=2)
plt.grid(1)
plt.title("Summation of Sinusoids")
plt.tight_layout()