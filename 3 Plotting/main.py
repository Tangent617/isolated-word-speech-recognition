from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt

rate, data = read("x.wav")
time = np.linspace(0, len(data) / rate, num = len(data))

f1 = plt.figure(1)
plt.plot(time, data)
plt.ylabel("Amplitude")
plt.xlabel("Time/s")
plt.show()
f1.savefig("x.jpg")