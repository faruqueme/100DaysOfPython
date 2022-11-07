#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
asd=input("What was the total bill? $")
Bill=float(asd)

sad=input("What percentage tip would you like to give? e.g. 10, 12, or 15? %")
percentage_tip= float(sad)
ten_percentage_tip= round(Bill*(percentage_tip/100)+Bill, 2)

uo=input("How many people to split the bill? ")
split_bill=float(uo)
final_1=round(ten_percentage_tip/split_bill, 2) 

print(f"Each person should pay ${final_1}")