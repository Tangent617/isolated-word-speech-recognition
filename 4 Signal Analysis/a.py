from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
from endpoint_detect import EndPointDetect

rate, data = read("x.wav")
time = np.linspace(0, len(data) / rate, num = len(data))
data_left = data[:,0]
data_right = data[:,1]
data_speech = EndPointDetect(data_left).wave_data_detected
windows = 256
m = 0

f1 = plt.figure(1)
plt.plot(time, data)
plt.ylabel("Amplitude")
plt.xlabel("Time/s")

while m < len(data_speech):
    begin = int(data_speech[m] * windows)
    end = int(data_speech[m + 1] * windows)

    m = m + 2
    # 滤去长度过短的片段
    if end - begin < 0.05 * 48000:
        continue

    plt.axvline(x=begin/rate, color='#2ca02c', label='T1') 
    plt.axvline(x=end/rate, color='#d62728', label='T2')

plt.legend()
plt.show()
f1.savefig("x_wav.jpg")