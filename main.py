import multiprocessing as mp
from algorithms.genetic_algorithm import genetic_algorithm
from utils.distance import distance
from config.config import NUM_ISLANDS, GENS, MIGRATION_INTERVAL

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
    print(f"Best solution found: {best_solution}, Distance: {distance(best_solution)}")

if __name__ == "__main__":
    run_parallel_ga()
