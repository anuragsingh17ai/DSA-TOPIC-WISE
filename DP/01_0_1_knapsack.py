"""
Fractional Knapsack:
--------------------
In the fractional knapsack problem, you can take fractions of items. This means you can split items into smaller parts, and take any portion of an item's weight. The objective is to maximize the total value of the knapsack while staying within a weight limit. This problem can be solved using a greedy algorithm, where items are selected based on their value-to-weight ratio, and the most valuable fractions are taken first until the knapsack is full.

0-1 Knapsack:
-------------
In the 0-1 knapsack problem, each item can either be taken as a whole or left. You cannot take fractional parts of an item. The objective is to maximize the total value of the knapsack without exceeding the weight capacity. This problem is typically solved using dynamic programming, where a table is constructed to keep track of the maximum value that can be obtained with different capacities and sets of items.

Unbounded Knapsack:
-------------------
The unbounded knapsack problem allows for an unlimited number of each type of item to be used. You can take as many instances of each item as you want, as long as the total weight does not exceed the knapsack's capacity. The goal is to maximize the total value. Like the 0-1 knapsack, this problem is also solved using dynamic programming, but with the key difference that each item can be chosen multiple times.
"""


