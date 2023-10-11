def sum_of_lists(n):
    total = 0
    for i in range(5):
        L = [j ^ (j >> i) for j in range(n)]
        total += sum(L)
        del L # remove reference to L
    return total

# Example taken from: https://jakevdp.github.io/PythonDataScienceHandbook/01.07-timing-and-profiling.html
