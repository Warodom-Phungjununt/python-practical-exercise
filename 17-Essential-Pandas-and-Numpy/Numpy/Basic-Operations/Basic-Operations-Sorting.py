# Sorting
import numpy as np

revenue = [123, 5, 33, 10, 12, 20, 40, 1.2, 9.9, 0.5, 11.11, 999]
cost = [10, 15, 100, 10, 5, 2, 13.1, 10, 99, 0, 3.2, 555] 
revenue = np.array(revenue)
cost = np.array(cost)
profit = revenue - cost

# Sort profits from lowest to highest. Enter the profit_sorted variable.
profit_sorted = np.sort(profit)
print(profit)
print(profit_sorted)

# Sort profits from highest to lowest. Enter the profit_reverse variable.
profit_reverse = sorted(profit, reverse=True)
profit_reverse = np.array(profit_reverse)
print(profit_reverse)
print(profit_reverse.dtype)