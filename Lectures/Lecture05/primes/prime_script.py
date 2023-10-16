# prime() function.

def prime(N):
    '''A function to find all the N prime numbers.

    Parameters
    ----------
    N : int
        The number of prime numbers that required to get.

    Returns
    -------
    primes : list
        The list of prime numbers.

    >>> prime(5)
    [2, 3, 5, 7, 11]

    >>> prime(7)
    [2, 3, 5, 7, 11, 13, 17]
    '''
    # python -m doctest prime.py -v
    test = 2
    primes = []
    while len(primes) < N:
        for p in primes:
            if p**2 > test:
                primes.append(test)
                break
            if test % p == 0:
                break
        # special case
        if len(primes) == 0:
            primes.append(test)
        test += 1
    print(primes)
