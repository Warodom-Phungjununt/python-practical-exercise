# Statistics
import numpy as np

revenue = [123, 5, 33, 10, 12, 20, 40, 1.2, 9.9, 0.5, 11.11, 999]
cost = [10, 15, 100, 10, 5, 2, 13.1, 10, 99, 0, 3.2, 555] 
revenue = np.array(revenue)
cost = np.array(cost)
profit = revenue - cost

# Find total income, total costs, and retained profits throughout the year.
total_revenue = np.sum(revenue) # revenue.sum()
total_cost = np.sum(cost) # cost.sum()
total_profit = np.sum(profit) # profit.sum()
print('Total revenue: {:,.2f}'.format(total_revenue))
print('Total cost: {:,.2f}'.format(total_cost))
print('Total profit(loss): {:,.2f}'.format(total_profit))

# Find the mean, median, and standard deviation of your income.
mean_revenue = np.mean(revenue)
median_revenue = np.median(revenue)
std_revenue = np.std(revenue)
print('Mean revenue: {:,.2f}'.format(mean_revenue))
print('Median revenue: {:,.2f}'.format(median_revenue))
print('Std revenue: {:,.2f}'.format(std_revenue))