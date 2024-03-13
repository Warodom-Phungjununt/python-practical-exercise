### Topic : Break/Continue/Pass Statement 1
# Generate a lottery program which receive 2 digit number
# If you win the lottery, print "Congratulation you won"
# If you don't win the lottery, print "woww"
# But when the user type higher than 99, stop the program

lottery_prize = 69

while True:
    number = input("Type your lottery number: ")
    number = int(number)

    if number > 99:
        print("Quit Program")
        break
    elif number == lottery_prize:
        print("Congratulation you won")
    else:
        print("woww")