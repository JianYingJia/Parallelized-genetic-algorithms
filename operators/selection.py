import numpy as np

"""
选择
"""
def select(population, fitness_values):
    probabilities = fitness_values / np.sum(fitness_values)
    indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return [population[i] for i in indices]
