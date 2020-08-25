from typing import Optional, List

# Recursive function
def fib_rec(n: int) -> int:
    # base case
    if n == 0 or n == 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


# Dynamic function
def fib_dyn(n: int) -> int:
    # base case
    if n == 0 or n == 1:
        return n
    # Instantiate Cache information

    cache_size = 10
    cache: List[Optional[int]]
    cache = [None] * (cache_size + 1)

    cache[0] = 0
    cache[1] = 1
    current_num = 2

    while current_num < n:
        cache[current_num % cache_size] = (
            cache[(current_num - 1) % cache_size]
            + cache[(current_num - 2) % cache_size]
        )
        current_num += 1

    return cache[(n - 1) % cache_size] + cache[(n - 2) % cache_size]


# Iterative function
def fib_iter(n: int) -> int:
    # base case
    if n == 0 or n == 1:
        return n
    phi = (1 + 5 ** 0.5) / 2
    psi = 1 - phi
    return round((phi ** n - psi ** n) / 5 ** 0.5)


def fib_iter2(n: int) -> int:
    # Set starting point
    a = 0
    b = 1

    # Follow algorithm
    for _ in range(n):
        a, b = b, a + b

    return a
