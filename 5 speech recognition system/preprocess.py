import numpy as np

def CMN(r):
    """
    Normalization
    :param r:
    :return:
    """
    return r - np.mean(r, axis=1, keepdims=True)