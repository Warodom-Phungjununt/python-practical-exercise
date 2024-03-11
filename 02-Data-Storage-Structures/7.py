### Create key for collecting your age and your idol's age
# Given key as a name and value as a year
birth = {
    'TheDome':28,
    'Ninoy':45,
    'Arm':30,
    'TheMeen':31
}
print(birth)

# Call age of each person
print("TheDome is ",birth['TheDome']," years old")
print("Ninoy is ",birth['Ninoy']," years old")
print("Arm is ",birth['Arm']," years old")
print("TheMeen is ",birth['TheMeen']," years old")

# Add PeeTa who is 39 years old
birth['PeeTa'] = 39
print(birth)

# Remove PeeTa by pop
print(birth.pop('PeeTa'))
print(birth)