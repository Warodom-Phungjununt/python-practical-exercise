#Create List for showing these number
#[1, 2, 4, 8, 16, ..., 256]
#To a variable name "doubling numbers"

doubling_numbers = [2**i for i in range(9)]
print(doubling_numbers)

#Given list of dollar money
money_usd = [1.50, 20, 99, 0, 69.69]

#Create Thai Baht new list
#Given 1usd = 32.50 thb
money_thb = [money*32.50 for money in money_usd]
print(money_thb)