### Topic : While Loop 1
# Satring with money 20 baht
# Mom gives me 35 baht for a snack
# How long will I have more than 1000 Baht
# How many

current_money = 20
n_days = 0

while current_money <= 1000:
    current_money = current_money + 35
    n_days = n_days + 1
    print("Day ",n_days,": My money is ",current_money)

print("Finally, I spend ",n_days," days to earn more than 1000 baht")