import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
import numpy as np

rate, data = wav.read('x.wav')
data_seg1 = data[int(0.5*rate):int(0.52*rate)]
N = int(0.02 * rate)

fft_y=np.fft.fft(data_seg1, axis = 0)
fft_x=np.fft.fftfreq(N, 1 / rate)

f1 = plt.figure(1)
plt.title("Seg1 FFT")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.plot(fft_x, np.abs(fft_y))
plt.show()
f1.savefig('fourier_x_np.jpg')