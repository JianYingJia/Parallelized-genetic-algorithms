import numpy as np
import multiprocessing as mp
from utils.fitness import fitness
from utils.distance import distance
from utils.population import initialize_population
from operators.selection import select
from operators.crossover import crossover
from operators.mutation import mutate
from config.config import POP_SIZE, GENS, MIGRATION_INTERVAL, NUM_ISLANDS

# def genetic_algorithm(island_id, queue):
#     """
#     基因算法
#     :param island_id: 群岛ID
#     :param queue: 消息队列
#     """
#     population = initialize_population(POP_SIZE)

#     for generation in range(GENS):
#         fitness_values = np.array([fitness(ind) for ind in population])
#         selected = select(population, fitness_values)

#         # 交叉和变异
#         next_population = []
#         for i in range(0, len(selected) - 1, 2):
#             child1 = crossover(selected[i], selected[i + 1])
#             next_population.append(mutate(child1))

#         # 处理奇数个体
#         if len(selected) % 2 == 1:
#             next_population.append(selected[-1])

#         population = next_population

#         if generation % MIGRATION_INTERVAL == 0:
#             best_individual = population[np.argmax(fitness_values)]
#             queue.put((island_id, best_individual))

#     best_route = population[np.argmax([fitness(ind) for ind in population])]
#     queue.put((island_id, best_route))

def genetic_algorithm(island_id, queue):
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

        if generation % MIGRATION_INTERVAL == 0:
            best = population[np.argmax([fitness(ind) for ind in population])]
            queue.put((island_id, best))

    best = population[np.argmax([fitness(ind) for ind in population])]
    queue.put((island_id, best))

def run_parallel_ga():
    queue = mp.Queue()
    processes = [mp.Process(target=genetic_algorithm, args=(i, queue)) for i in range(NUM_ISLANDS)]

    for p in processes:
        p.start()

    migration_pool = []
    for _ in range(NUM_ISLANDS * (GENS // MIGRATION_INTERVAL + 1)):
        island_id, best_individual = queue.get()
        migration_pool.append((island_id, best_individual))

    for p in processes:
        p.join()

    best_solution = min(migration_pool, key=lambda x: distance(x[1]))[1]
    print(f"[Parallel] Best solution: {best_solution}")
    print(f"[Parallel] Distance: {distance(best_solution):.4f}")
