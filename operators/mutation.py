import numpy as np
from config.config import MUTATION_RATE

def mutate(individual):
    """
    变异
    :param individual: 待变异的个体
    :return: 变异后的个体
    """
    # 如果随机数小于变异率，则进行变异操作
    if np.random.rand() < MUTATION_RATE:
        # 随机选择两个位置
        i, j = np.random.randint(0, len(individual), 2)
        # 交换两个位置的值
        individual[i], individual[j] = individual[j], individual[i]
    # 返回变异后的个体
    return individual
