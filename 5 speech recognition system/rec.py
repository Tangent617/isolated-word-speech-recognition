from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from librosa.feature import mfcc
from preprocess import *
from mydtw import *

features = {}
for i in range(6):
    fs, data = read('../1 template data/S{}A.wav'.format(i+1))
    speechIn1 = data[:,0]
    fm_a = mfcc(y=speechIn1.astype('float'), sr=fs, n_mfcc=13)
    features['S{}A'.format(i+1)] = CMN(fm_a)

scores = []
for j in range(6):
    fs, data = read('../2 testing data/S{}B.wav'.format(j+1))
    speechIn1 = data[:,0]
    fm_b = mfcc(y=speechIn1.astype('float'), sr=fs, n_mfcc=13)
    scores.append(DTWScores(CMN(fm_b), features, 6))

np.savetxt("confusion matrix.csv", scores, delimiter=",")
f1 = plt.figure(1)
plt.imshow(scores)
plt.title('Confusion Matrix')
plt.ylabel('Actual class')
plt.xlabel('Predicted class')
plt.colorbar()
plt.show()
f1.savefig('confusion matrix.jpg')