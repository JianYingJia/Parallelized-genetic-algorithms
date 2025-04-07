import numpy as np
from config.config import cities, NUM_CITIES, POP_SIZE, GENS, MUTATION_RATE, CROSSOVER_RATE

# 计算路径距离
def distance(route):
    return sum(np.linalg.norm(cities[route[i]] - cities[route[i + 1]]) for i in range(len(route) - 1)) + np.linalg.norm(cities[route[-1]] - cities[route[0]])

# 适应度函数
def fitness(route):
    return 1 / distance(route)

# 初始化种群
def initialize_population(size):
    return [np.random.permutation(NUM_CITIES) for _ in range(size)]

# 轮盘赌选择
def select(population, fitness_values):
    probabilities = fitness_values / np.sum(fitness_values)
    indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return [population[i] for i in indices]

# PMX交叉
def crossover(parent1, parent2):
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

# 交换变异
def mutate(individual):
    if np.random.rand() < MUTATION_RATE:
        i, j = np.random.randint(0, len(individual), 2)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

# 串行遗传算法主函数
def genetic_algorithm_serial():
    population = initialize_population(POP_SIZE)

    for generation in range(GENS):
        fitness_values = np.array([fitness(ind) for ind in population])
        selected = select(population, fitness_values)

        next_population = []
        for i in range(0, len(selected) - 1, 2):
            child1 = crossover(selected[i], selected[i + 1])
            next_population.append(mutate(child1))

        if len(selected) % 2 == 1:
            next_population.append(selected[-1])

        population = next_population

        # 可选：每隔一定代数打印当前最优
        if generation % 20 == 0:
            best_idx = np.argmax([fitness(ind) for ind in population])
            print(f"Generation {generation}, Distance: {distance(population[best_idx]):.4f}")

    best = min(population, key=distance)
    print(f"Best solution found: {best}")
    print(f"Distance: {distance(best):.4f}")

# 运行主程序
if __name__ == "__main__":
    genetic_algorithm_serial()
