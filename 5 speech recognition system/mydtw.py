from dtw import dtw
import numpy as np

manhattan_distance = lambda x, y: np.abs(x - y)

def DTWScores(r, features, N):
    """
    DTW find the min distortion
    :param r: MFCC matrix
    :param features: features
    :param N: word counts
    :return:
    """
    
    scores = np.zeros(N)

    for i in range(N):
        x = features['S{}A'.format(i+1)].reshape(-1, 1)
        y = r.reshape(-1, 1)
        d, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=manhattan_distance)
        scores[i] = d
    return scores