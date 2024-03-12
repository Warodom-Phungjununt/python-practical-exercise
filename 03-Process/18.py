### Topic : For Loop 2
# Given list

money_usd = [1.50, 20, 99, 0, 69.69]

# Generate new list named "money_ttb" which convert dollar to baht
# 1 USD = 32.50 Baht

money_thb = []

for usd in money_usd:
    print('Money in USD is ', usd)
    thb = usd * 32.50
    money_thb = money_thb + [thb]
    # print('-> Money in THB is ', money_thb)
    print(money_thb)