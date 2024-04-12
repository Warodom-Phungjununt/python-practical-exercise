# Basic Slicing
import numpy as np

revenue = [123, 5, 33, 10, 12, 20, 40, 1.2, 9.9, 0.5, 11.11, 999]
cost = [10, 15, 100, 10, 5, 2, 13.1, 10, 99, 0, 3.2, 555] 
revenue = np.array(revenue)
cost = np.array(cost)
profit = revenue - cost

# Record profits during quarter 1-4 into variables profit_Q1, ..., profit_Q4
profit_Q1 = profit[:3]
profit_Q2 = profit[3:6]
profit_Q3 = profit[6:9]
profit_Q4 = profit[9:]
print(profit_Q1)
print(profit_Q2)
print(profit_Q3)
print(profit_Q4)

# Which quarter is the most profitable?
profit_Q1_sum = np.sum(profit_Q1)
profit_Q2_sum = np.sum(profit_Q2)
profit_Q3_sum = np.sum(profit_Q3)
profit_Q4_sum = np.sum(profit_Q4)
profit_sum = sorted(np.array([profit_Q1_sum, profit_Q2_sum, profit_Q3_sum, profit_Q4_sum]), reverse=True)
print(profit_sum)
print(f"The maximum profit is Quarter 4 which is {profit_sum[0]} million Baht")