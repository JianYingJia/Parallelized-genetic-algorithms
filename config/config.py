import numpy as np

# 城市数量
NUM_CITIES = 20
# 种群大小
POP_SIZE = 100
# 迭代次数
GENS = 200
# 变异率
MUTATION_RATE = 0.2
# 交叉率
CROSSOVER_RATE = 0.8
# 岛群数量
NUM_ISLANDS = 4
# 迁移间隔
MIGRATION_INTERVAL = 20

# 随机生成城市坐标
np.random.seed(42)
cities = np.random.rand(NUM_CITIES, 2)
