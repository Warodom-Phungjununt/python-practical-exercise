### Topic : For Loop 3
# Given dict
famous_people = {
    'Great': 32,
    'Jennie': 27,
    'Elon': 52
    }

# Use for-loop to print name and age
for name, age in famous_people.items():
    print(name + ' is ' + str(age) + ' years old.')

#Who is the youngest by using for-loop
min_age = 1000
min_age_name = None
for name, age in famous_people.items():
    if age < min_age:
        min_age_name = name
        min_age = age

print("The youngest member is ",min_age_name," who is ",min_age," years old")