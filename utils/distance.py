import numpy as np
from config.config import cities


def distance(route):
    """
    距离计算
    """
    return sum(np.linalg.norm(cities[route[i]] - cities[route[i + 1]]) for i in range(len(route) - 1)) + \
           np.linalg.norm(cities[route[-1]] - cities[route[0]])
