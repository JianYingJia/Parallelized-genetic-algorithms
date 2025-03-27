import numpy as np
from config.config import cities


"""
距离计算
"""
def distance(route):
    return sum(np.linalg.norm(cities[route[i]] - cities[route[i + 1]]) for i in range(len(route) - 1)) + \
           np.linalg.norm(cities[route[-1]] - cities[route[0]])
