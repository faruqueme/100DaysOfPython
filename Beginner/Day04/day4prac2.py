# # 🚨 Don't change the code below 👇
# import random
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# 
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
# 
# #Write your code below this line 👇
# import random
# select_names=random.choices(names)
# 
# #(','.join) is used to remov brackets from output.
# 
# nice=','.join(select_names)
# print(f"{nice} is going to buy the meal today!")


######## Another process


# # 🚨 Don't change the code below 👇
# import random
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# 
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
# 
# #Write your code below this line 👇
# import random
# select_names=random.choices(names)
# 
# #(','.join) is used to remove brackets from output.
# 
# nice=','.join(select_names)
# print(f"{nice} is going to buy the meal today!")
# 


########


# import random
# 
# # Split string method
# names_string = input("Give me everybody's names, seperated by a comma. ")
# names = names_string.split(", ")
# 
# #Write your code below this line 👇
# 
# #Get the total number of items in list.
# num_items = len(names)
# #Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# #Pick out random person from list of names using the random number.
# person_who_will_pay = names[random_choice]
# 
# print(person_who_will_pay + " is going to buy the meal today!")
