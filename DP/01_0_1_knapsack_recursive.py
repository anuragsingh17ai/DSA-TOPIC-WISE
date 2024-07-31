"""
Identification of DP: choice and optimal (min, max)
DP = Recursion + Storage

Fractional Knapsack:
--------------------
In the fractional knapsack problem, items can be divided, allowing fractions to be taken. The goal is to maximize the total value without exceeding the weight limit, typically solved using a greedy algorithm based on the value-to-weight ratio.

0-1 Knapsack:
-------------
In the 0-1 knapsack problem, each item can either be taken or left whole. The objective is to maximize the total value within the weight limit, usually solved using dynamic programming.

Unbounded Knapsack:
-------------------
In the unbounded knapsack problem, an unlimited number of each item is available. The goal is to maximize the total value, solved using dynamic programming where items can be chosen multiple times.
"""

def knapsack(wt: list[int], val: list[int], w: int, n: int) -> int:
    """
    Solves the 0-1 Knapsack problem using a recursive approach.

    Args:
    wt (list[int]): Weights of the items.
    val (list[int]): Values of the items.
    w (int): Maximum weight capacity of the knapsack.
    n (int): Number of items.

    Returns:
    int: The maximum value that can be obtained.
    """
    # Base case: If no items are left or the capacity is zero
    if n == 0 or w == 0:
        return 0

    # If the weight of the nth item is less than or equal to the capacity
    if wt[n - 1] <= w:
        # Choose the maximum of including or excluding the nth item
        include_item = val[n - 1] + knapsack(wt, val, w - wt[n - 1], n - 1)
        exclude_item = knapsack(wt, val, w, n - 1)
        return max(include_item, exclude_item)
    else:
        # Exclude the nth item if its weight is more than the capacity
        return knapsack(wt, val, w, n - 1)
