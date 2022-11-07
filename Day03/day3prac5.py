# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# For Love Scores less than 10 or greater than 90, the message should be:
# 
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# 
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# 
# "Your score is **z**."
name_1=name1.lower()
name_2=name2.lower()
T_1=name_1.count('t')
R_1=name_1.count('r')
U_1=name_1.count('u')
E_1=name_1.count('e')
L_1=name_1.count('l')
O_1=name_1.count('o')
V_1=name_1.count('v')


T_2=name_2.count('t')
R_2=name_2.count('r')
U_2=name_2.count('u')
E_2=name_2.count('e')
L_2=name_2.count('l')
O_2=name_2.count('o')
V_2=name_2.count('v')

Add_1=T_1+R_1+U_1+E_1
Add_2=T_2+R_2+U_2+E_2
Add_3=L_1+O_1+V_1+E_1
Add_4=L_2+O_2+V_2+E_2

true_add=Add_1+Add_2
love_add=Add_3+Add_4
x=str(true_add) + str(love_add)
final=int(x)
if final>90 or final<10:
	print(f"Your score is {x}, you go together like coke and mentos.")
	
elif final>=40 and final<=50:
	print(f"Your score is {x}, you are alright together.")
	
else :
	print(f"Your score is {x}.")
	