from utils.distance import distance



def fitness(route):
    """
    适应度计算
    """
    return 1 / distance(route)
