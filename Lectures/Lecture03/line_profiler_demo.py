import math
import random


@profile
def random_list(n):
    return [2*random.random() - 1 for _ in range(n)]


@profile
def distance(x, y):
    return math.sqrt(x**2 + y**2)


@profile
def estimate_pi(n):
    x_list = random_list(n)
    y_list = random_list(n)
    
    in_circle = 0
    for x, y in zip(x_list, y_list):
        if distance(x, y) <= 1:
            in_circle += 1
            
    return 4*in_circle / n


if __name__ == '__main__':
    estimate_pi(1_000_000)
