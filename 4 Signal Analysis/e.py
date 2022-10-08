import numpy as np
from scipy.io import wavfile as wav
from scipy.signal import filtfilt
from matplotlib import pyplot as plt

def lpc_coeff(s, p):
    """
    :param s: a frame
    :param p: order of linear prediction
    :return:
    """
    n = len(s)
    # Autocorrelation
    Rp = np.zeros(p)
    for i in range(p):
        Rp[i] = np.sum(np.multiply(s[i + 1:n], s[:n - i - 1]))
    Rp0 = np.matmul(s, s.T)
    Ep = np.zeros((p, 1))
    k = np.zeros((p, 1))
    a = np.zeros((p, p))
    # i=0
    Ep0 = Rp0
    k[0] = Rp[0] / Rp0
    a[0, 0] = k[0]
    Ep[0] = (1 - k[0] * k[0]) * Ep0
    # start from i=1, Recursion
    if p > 1:
        for i in range(1, p):
            k[i] = (Rp[i] - np.sum(np.multiply(a[:i, i - 1], Rp[i - 1::-1]))) / Ep[i - 1]
            a[i, i] = k[i]
            Ep[i] = (1 - k[i] * k[i]) * Ep[i - 1]
            for j in range(i - 1, -1, -1):
                a[j, i] = a[j, i - 1] - k[i] * a[i - j - 1, i - 1]
    ar = np.zeros(p + 1)
    ar[0] = 1
    ar[1:] = -a[:, p - 1]
    # G = np.sqrt(Ep[p - 1])
    return ar#, G

rate, data = wav.read('x.wav')
data_left = data[:,0]
data_right = data[:,1]
data_seg1 = data_left[int(0.5*rate):int(0.52*rate)]
data_seg1_len = int(0.02 * rate)
time = np.linspace(0, len(data_seg1) / rate, num = len(data_seg1))
lpc_order = 10

ar = lpc_coeff(data_seg1, lpc_order)
ar[0] = 0
est_x = filtfilt(-ar, [1], data_seg1)

f = open('lpc10.txt', 'w')
print(ar, file=f)
f.close()

# 看看与原数据区别，自用
plt.plot(time, data_seg1, 'k')
plt.plot(time, est_x, 'c')
plt.title('LPC decoder')
plt.legend(['original signal', 'decoded signal'])
plt.show()

# reference https://github.com/busyyang/python_sound_open/blob/master/chapter3_分析实验/lpc.py