import numpy as np
from utils.fitness import fitness
from utils.population import initialize_population
from operators.selection import select
from operators.crossover import crossover
from operators.mutation import mutate
from config.config import POP_SIZE, GENS, MIGRATION_INTERVAL

def genetic_algorithm(island_id, queue):
    population = initialize_population(POP_SIZE)

    for generation in range(GENS):
        fitness_values = np.array([fitness(ind) for ind in population])
        selected = select(population, fitness_values)

        # 交叉和变异
        next_population = []
        for i in range(0, len(selected) - 1, 2):
            child1 = crossover(selected[i], selected[i + 1])
            next_population.append(mutate(child1))

        # 处理奇数个体
        if len(selected) % 2 == 1:
            next_population.append(selected[-1])

        population = next_population

        if generation % MIGRATION_INTERVAL == 0:
            best_individual = population[np.argmax(fitness_values)]
            queue.put((island_id, best_individual))

    best_route = population[np.argmax([fitness(ind) for ind in population])]
    queue.put((island_id, best_route))
