import numpy as np
from utils.population import initialize_population
from utils.distance import distance
from utils.fitness import fitness
from operators.selection import select
from operators.crossover import crossover
from operators.mutation import mutate
from config.config import POP_SIZE, GENS

def genetic_algorithm_serial():
    population = initialize_population(POP_SIZE)

    for generation in range(GENS):
        fitness_values = np.array([fitness(ind) for ind in population])
        selected = select(population, fitness_values)

        next_population = []
        for i in range(0, len(selected) - 1, 2):
            child = crossover(selected[i], selected[i + 1])
            next_population.append(mutate(child))
        if len(selected) % 2 == 1:
            next_population.append(selected[-1])
        population = next_population

        if generation % 20 == 0:
            best = min(population, key=distance)
            # print(f"[Serial] Generation {generation} Best Distance: {distance(best):.4f}")

    best = min(population, key=distance)
    print(f"[Serial] Final Best Route: {best}")
    print(f"[Serial] Final Best Distance: {distance(best):.4f}")
