# Boolean Indexing
import numpy as np

revenue = [123, 5, 33, 10, 12, 20, 40, 1.2, 9.9, 0.5, 11.11, 999]
cost = [10, 15, 100, 10, 5, 2, 13.1, 10, 99, 0, 3.2, 555] 
revenue = np.array(revenue)
cost = np.array(cost)
profit = revenue - cost
months = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Which months are loss ?
loss_months_indices = (profit<0)
print(f"Losses are occured in {months[loss_months_indices]}")

# Find the index
loss_months_indices_2 = np.argwhere(profit<0)
print(f"Find loss months by using other method are occured in {months[loss_months_indices_2]}")

# How much loss
for i in range(12):
    if loss_months_indices[i] == True:
        print(months[i], ": ", profit[i])

# How much profit
for i in range(12):
    if loss_months_indices[i] == False:
        print(months[i], ": ", profit[i])

# Which months has profit higher than 50 or lower than 0
months_indices = (profit>50) | (profit<0)
print("Which months has profit higher than 50 or lower than 0")
for i in range(12):
    if months_indices[i] == True:
        print(months[i], ": ", profit[i])