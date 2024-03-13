### Topic : Defining and Calling Function 2
# Defining function for calculating BMI

def BMI_calculator(weight_kg,height_cm):
    height_m = height_cm/100
    BMI = weight_kg/(height_m**2)
    return BMI

weight = input("Give me your weight in Kilogram: ")
height = input("Give me your height in Centimeter: ")
weight = int(weight)
height = int(height)
BMI = BMI_calculator(weight,height)
print("Your BMI is ", BMI)