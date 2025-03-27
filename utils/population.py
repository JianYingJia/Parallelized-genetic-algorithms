import numpy as np
from config.config import NUM_CITIES


"""
初始化种群
"""
def initialize_population(size):
    return [np.random.permutation(NUM_CITIES) for _ in range(size)]
