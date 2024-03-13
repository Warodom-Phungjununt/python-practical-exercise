### Topic : Defining and Calling Function
# Defining function for greeting TheDome
# By printing Hello, TheDome

def greet_TheDome():
    print("Hello, TheDome")

greet_TheDome()

# Defining function named "greet"
# Get an input as a name
# When this function was called, it will print a message for greeting them
# If he is TheDome, print "Hi Bro, TheDome is coming"

def greet(name):
    if name == 'TheDome':
        print("Hi Bro, TheDome is coming")
    else:
        print("Hello, ", name)

input_name = input("Give me your name: ")
greet(input_name)
