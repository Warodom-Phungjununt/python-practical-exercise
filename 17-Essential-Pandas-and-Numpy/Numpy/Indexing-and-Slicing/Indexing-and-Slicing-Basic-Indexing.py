# Basic Indexing
import numpy as np

revenue = [123, 5, 33, 10, 12, 20, 40, 1.2, 9.9, 0.5, 11.11, 999]
cost = [10, 15, 100, 10, 5, 2, 13.1, 10, 99, 0, 3.2, 555] 
revenue = np.array(revenue)
cost = np.array(cost)
profit = revenue - cost

# Profit from November
print(profit[10])

#กำไรของเดือนที่ลงท้ายด้วย "คม" เป็นอย่างไร
profit_specific_month = np.array([profit[0], profit[2], profit[4], profit[6], profit[7], profit[9], profit[11]])
print(profit_specific_month)

# Another method
kom_months = np.array([1, 3, 5, 7, 8, 10, 12])
kom_indices = kom_months - 1
print(profit[kom_indices])