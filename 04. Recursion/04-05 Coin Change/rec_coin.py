from typing import List, Optional

# Greedy method
def rec_coin(target: int, coins: List[int]) -> Optional[int]:
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
