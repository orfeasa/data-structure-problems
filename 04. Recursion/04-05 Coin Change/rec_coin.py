from typing import List, Optional


# Dynamic method
def rec_coin(target: int, coins: List[int]) -> int:

    # Initialize a list where we will store the known solutions
    # Initial value will be a value that is too high (infinity)
    # We need a list of target + 1 slots so that known_solutions[target]
    # becomes our final answer
    known_solutions = [float("inf")] * (target + 1)

    known_solutions[0] = 0

    coins.sort()
    coins_set = set(coins)
    # we will now build the entire known_solutions list until we reach the end
    for amount in range(target + 1):
        # if we have a coin with that amount
        if amount in coins_set:
            known_solutions[amount] = 1
        else:
            for coin in coins:
                if coin > amount:
                    # This coin is too large.
                    # All subsequent coins will also be too large (sorted list)
                    break
                else:
                    # Simulate taking the coin and see if it offers a better
                    # solution than the current one
                    known_solutions[amount] = min(
                        known_solutions[amount], 1 + known_solutions[amount - coin]
                    )
    return known_solutions[target]


# Greedy method. Does not work for every case
def rec_coin_greedy(target: int, coins: List[int]) -> Optional[int]:
    coins.sort(reverse=True)

    # base case
    if target == 0:
        return 0

    if target in coins:
        return 1

    # If the target is smaller than the smallest coin, it's not solvable
    if target < coins[-1]:
        return None

    for coin in coins:
        if coin <= target:
            sub_case = rec_coin(target - coin, coins)
            if sub_case is None:
                return None
            return 1 + sub_case
