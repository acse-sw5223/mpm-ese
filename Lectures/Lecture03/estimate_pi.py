import math
import random


def random_list(n):
    """Create a list with n elements, with each
    element with value between -1 and 1.
    
    Parameters
    ----------
    n : int
        The number of elements.
        
    Return
    ------
    list(float)
    
    """
    return [2*random.random() - 1 for _ in range(n)]


def distance(x, y):
    """Compute the distance from the origin of a point with coordinates x and y.
    
    Parameters
    ----------
    n : int
        The number of elements.
        
    Return
    ------
    float
        Distance from origin.

    """
    return math.sqrt(x**2 + y**2)


def estimate_pi(n):
    """Estimate the value of pi using Monte Carlo simulation.
    
    Parameters
    ----------
    n : int
        The number of random points generated.
        
    Returns
    -------
    float
        An estimate of pi.

    """
    x_list = random_list(n)
    y_list = random_list(n)
    
    in_circle = 0
    for x, y in zip(x_list, y_list):
        if distance(x, y) <= 1:
            in_circle += 1
            
    return 4*in_circle / n