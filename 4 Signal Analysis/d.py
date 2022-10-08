import numpy as np
from scipy.io import wavfile as wav
from matplotlib import pyplot as plt

def pre_emphasis(signal, coeff):
    return np.append(signal[0], signal[1:] - coeff * signal[:-1])

def plot_aLL(x, y, location, title):
    plt.subplot(location)
    plt.plot(x, y)
    plt.xlabel('Time/s')
    plt.ylabel('Ampltitude')
    plt.title(title)
    plt.tight_layout()

rate, data = wav.read('x.wav')
data_left = data[:,0]
data_right = data[:,1]
data_seg1 = data_left[int(0.5*rate):int(0.52*rate)]
time = np.linspace(0, len(data_seg1) / rate, num = len(data_seg1))

f1 = plt.figure(1)
plot_aLL(time, data_seg1, 211, "Seg1")
plot_aLL(time, pre_emphasis(data_seg1, 0.95), 212, "Pem_Seg1")
f1.savefig("Pem_x.jpg")