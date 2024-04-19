# Arithmatics
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + 10)
print(a * 3)
print(a**2) #ยกกำลัง
print(a + b)
print(a * b)
print(a / b)
print(np.sqrt(a))

# Example: from revenue and cost
revenue = [123, 5, 33, 10, 12, 20, 40, 1.2, 9.9, 0.5, 11.11, 999]
cost = [10, 15, 100, 10, 5, 2, 13.1, 10, 99, 0, 3.2, 555] 

# Create an ndarray
revenue = np.array(revenue)
print(revenue)
cost = np.array(cost)
print(cost)

# Create an array named profit for calculating profit (or loss) for each month.
profit = revenue - cost
print(profit)
print(profit.dtype)

# Suppose that profit figures must be sent to be displayed in slides in US dollars.
# Use exchange rate 1 dollar = 31.5 baht
profit_us = profit/31.5
print(profit_us)