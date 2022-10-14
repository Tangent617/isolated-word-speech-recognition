from scipy.io.wavfile import read
from librosa.feature import mfcc
from preprocess import *
from mydtw import *
import matplotlib.pyplot as plt

# choose id'th recording
id = 1

# read data
fs, data_a = read('../1 template data/S{}A.wav'.format(id))
fs, data_b = read('../2 testing data/S{}B.wav'.format(id))
data_a_in1 = data_a[:,0]
data_b_in1 = data_b[:,0]

# mfcc
fm_a = mfcc(y=data_a_in1.astype('float'), sr=fs, n_mfcc=13)
fm_b = mfcc(y=data_b_in1.astype('float'), sr=fs, n_mfcc=13)

# normalization and reshape
fm_a = CMN(fm_a).reshape(-1, 1)
fm_b = CMN(fm_b).reshape(-1, 1)

# calculation
d, cost_matrix, acc_cost_matrix, path = dtw(fm_a, fm_b, dist=manhattan_distance)

# plot
f1 = plt.figure(1)
plt.imshow(cost_matrix.T, origin='lower')
plt.plot(path[0], path[1])
plt.show()
f1.savefig('optimal path.jpg')