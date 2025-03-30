import numpy as np
from config.config import NUM_CITIES


def initialize_population(size):
    """
    初始化种群
    """
    return [np.random.permutation(NUM_CITIES) for _ in range(size)]
