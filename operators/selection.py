import numpy as np

def select(population, fitness_values):
    """
    选择
    """
    probabilities = fitness_values / np.sum(fitness_values)
    indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return [population[i] for i in indices]
