# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆
# 
# #Write your code below this line 👇
# 
# str(age)
# years=90-int(age)
# str(years)
# months=int(years)*12
# str(months)
# months=years*12
# weeks=years*52
# str(weeks)
# days=years*365
# str(days)
# print(f"You have {days} days, {weeks} weeks, and {months} months left")

# another procedure
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
