# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

print("Enter your weight:")
weight = int(input())

print("Enter your height:")
height = float(input())

BMI = weight / (height ** 2)
BMI_as_int = int(BMI)
result = round(BMI_as_int, 0)
# print("Your Body Mass Index(BMI) is:", result)

# Printing using the f-string
print(f"Your Body Mass Index(BMI) is {result}")
