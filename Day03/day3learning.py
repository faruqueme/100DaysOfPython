# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# a=float((weight / (height)**2 ))
# BMI=round(a)
# if BMI == 40:
#     print(f"Your BMI is {BMI}, you are end.")
# elif BMI >= 33:
#    print(f"Your BMI is {BMI}, you are clinically obese.")
#         
# elif BMI >= 28:
#     print(f"Your BMI is {BMI}, you are obese.")
#         
# elif BMI >= 22:
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
#     
# elif BMI>=18:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# else :
#     print(f"Your BMI is {BMI}, you are underweight.")

# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# S=15
# M=20
# L=25
# Pepperoni_for_S = 2
# Pepperoni_for_M_L=3
# extra_cheese_cheese= 1
# small_pizza=S+Pepperoni_for_S+extra_cheese_cheese
# medium_pizza=M+Pepperoni_for_M_L+extra_cheese_cheese
# large_pizza=L+Pepperoni_for_M_L+extra_cheese_cheese
#  
# if size=="S"and add_pepperoni=="Y" and extra_cheese=="Y" :
#   print(f"Your Bill is ${small_pizza}.")
# elif size=="S" and add_pepperoni=="Y" and extra_cheese=="N":
#     small_pizza-=extra_cheese_cheese
#     print(f"Your Bill is ${small_pizza}.")
# elif size=="S" and add_pepperoni=="N" and extra_cheese=="Y":
#     small_pizza-=add_pepperoni
#     print(f"Your Bill is ${small_pizza}.")
# 
# # medium_pizza
# 
# elif  size=="M"and add_pepperoni=="Y" and extra_cheese=="Y" :
#   print(f"Your Bill is ${medium_pizza}.")
# elif size=="M" and add_pepperoni=="Y" and extra_cheese=="N":
#     medium_pizza-=extra_cheese_cheese
#     print(f"Your Bill is ${medium_pizza}.")
# elif size=="M" and add_pepperoni=="N" and extra_cheese=="Y":
#     medium_pizza-=Pepperoni_for_M_L
#     print(f"Your Bill is ${medium_pizza}.")
# 
# #large_pizza
#     
# elif  size=="L"and add_pepperoni=="Y" and extra_cheese=="Y" :
#   print(f"Your Bill is ${large_pizza}.")
# elif size=="L" and add_pepperoni=="Y" and extra_cheese=="N":
#     large_pizza-=extra_cheese_cheese
#     print(f"Your Bill is ${large_pizza}.")
# elif size=="L" and add_pepperoni=="N" and extra_cheese=="Y":
#     large_pizza-=Pepperoni_for_M_L
#     print(f"Your Bill is ${large_pizza}.")
# else:
#     print(f"Come back later.")
# 
# 
# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆
# 
# #Write your code below this line 👇

# from collections import Counter

# name1.lower()
# name2.lower()
# from collections import Counter
# name_1=Counter(name1)
# name_2=Counter(name2)
# 
# common_words=list(set(name_1)&set(name_2))
# print(len(common_words))





 









