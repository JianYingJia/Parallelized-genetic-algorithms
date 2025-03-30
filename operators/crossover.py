import numpy as np
from config.config import CROSSOVER_RATE

def crossover(parent1, parent2):
    """
    交叉
    :param parent1: 父代1
    :param parent2: 父代2
    :return: 子代
    """
    if np.random.rand() < CROSSOVER_RATE:
        size = len(parent1)
        p1, p2 = np.random.randint(0, size, 2)
        start, end = min(p1, p2), max(p1, p2)
        child = np.full(size, -1)
        child[start:end] = parent1[start:end]

        for i in range(start, end):
            if parent2[i] not in child:
                idx = i
                while child[idx] != -1:
                    idx = np.where(parent2 == parent1[idx])[0][0]
                child[idx] = parent2[i]

        child[child == -1] = [gene for gene in parent2 if gene not in child]
        return child
    return parent1.copy()
