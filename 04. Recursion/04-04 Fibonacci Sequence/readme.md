# Fibonnaci Sequence

## Problem

Implement a [Fibonnaci Sequence](https://en.wikipedia.org/wiki/Fibonacci_number) in three different ways:

- Recursively
- Dynamically (Using Memoization to store results)
- Iteratively

Your function will accept a number **n** and return the **nth** number of the fibonacci sequence

Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if n = 0 or 1, then it returns 1.

Else it returns fib(n-1)+fib(n+2).

## Code

### Recursively

Solve the problem using simple recursion.

```python
def fib_rec(n):
    pass
```

### Dynamically

Implement the function using dynamic programming by using a cache to store results (memoization).

```python
# Instantiate Cache information
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    pass
```

### Iteratively

Implement the solution with simple iteration.

```python
def fib_iter(n):
    pass
```
