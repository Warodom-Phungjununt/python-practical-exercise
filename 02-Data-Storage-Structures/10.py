# Given the personal information
name = "TheDome"
age = 28
facts = ['Like Data Science', 'Marathon', 'Love Aom']

TheDome = (name,age,facts)
print(TheDome)
print(len(TheDome))
print("He is ",TheDome[0])
print("He is ",TheDome[1]," years old")
print(TheDome[1:])

# Given additional information
is_youtuber = True
height = 170

# Add the additional information
TheDome = TheDome + (is_youtuber,height)
print(TheDome)

# Change the height in Tuple
# Basically, the value in the tuple cannot be change
# This task is going to edit TheDome's height
TheDome = TheDome[:-1] + (180,)
print(TheDome)

# Change the value in the list
TheDome[2][2] = "Aom is very cute"
print(TheDome)