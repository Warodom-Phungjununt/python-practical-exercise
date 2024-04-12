# Basic Indexing
import numpy as np

revenue = [123, 5, 33, 10, 12, 20, 40, 1.2, 9.9, 0.5, 11.11, 999]
cost = [10, 15, 100, 10, 5, 2, 13.1, 10, 99, 0, 3.2, 555] 
revenue = np.array(revenue)
cost = np.array(cost)
profit = revenue - cost

# Profit from November
print(profit[10])