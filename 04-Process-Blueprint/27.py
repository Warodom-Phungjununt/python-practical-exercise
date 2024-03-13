### Topic : Method 2
# Delete all whitespace at the front of sentence

channel = "    Heart   Rocker  "
channel = channel.lstrip()
print(channel)

#Given list named words
words = ['I','like','Hanni','from','New','Jeans']

# Take word in the list to a sentence
# Save in the my_sentence
print(" ".join(words) + '.')
print("".join(words) + '.')
print("$".join(words) + '.')

# Given an employee ID
employee_ID = 619

# Add 00 in front of the employee ID
employee_ID_complete = (str(employee_ID)).zfill(5)
print(employee_ID_complete)

# Given a list
names = ['Great','Tuty','Teddy','Tony','Timmy']
# Add 'Pommy' to the list
names.append('Pommy')
print(names)
# Remove the last member
removed_name = names.pop(0)
print(names)
print(removed_name)
# Remove Tony from the list
removed_Tony = names.remove('Tony')
print(names)
# Add TheDome to the list
updated_name = names.insert(-1, 'TheDome')
print(names)
# Sorting the name in the list
names.sort()
print(names)
names.sort(reverse=True)
print(names)