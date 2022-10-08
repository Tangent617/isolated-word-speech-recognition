import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
import numpy as np
import cmath

def omega(p, q):
   ''' The omega term in DFT and IDFT formulas'''
   return cmath.exp((2.0 * cmath.pi * 1j * q) / p)

def fft(x):
   ''' FFT of 1-d signals
   usage : X = fft(x)
   where input x = list containing sequences of a discrete time signals
   and output X = dft of x '''

   n = len(x)
   if n == 1:
      return x
   Feven, Fodd = fft(x[0::2]), fft(x[1::2])
   combined = [0] * n
   for m in range(int(n/2)):
     combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
     combined[int(m + n/2)] = Feven[m] - omega(n, -m) * Fodd[m]
   return combined

rate, data = wav.read('x.wav')
data_left = data[:,0]
data_right = data[:,1]
# a bit longer to make sure the length is power of 2
data_seg1 = data_left[int(0.5*rate):int(0.5*rate+1024)]
data_seg1_len = 1024

fft_y = fft(data_seg1)
rfft_y = fft_y[0:512]
label_x = np.linspace(0, int(data_seg1_len/2), int(data_seg1_len/2))
fft_x = label_x / data_seg1_len * rate

f1 = plt.figure(1)
plt.title("Seg1 FFT")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.plot(fft_x, np.abs(rfft_y))
plt.show()
f1.savefig('fourier_x.jpg')

# reference https://jeremykun.com/2012/07/18/the-fast-fourier-transform/