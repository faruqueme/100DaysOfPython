# print(3+3-3/3*3)

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
M = (str(height))
Kg = (str(weight))
meter = float(M)
kg = int(Kg)
int((kg / meter ** 2))
print("Your BMI is ", int(kg / meter ** 2))
# print("Your BMI is " ,int(kg / pow(m , 2)))
