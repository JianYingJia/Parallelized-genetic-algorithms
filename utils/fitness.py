from utils.distance import distance


"""
适应度计算
"""
def fitness(route):
    return 1 / distance(route)
