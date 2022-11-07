# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
S=15
M=20
L=25
Pepperoni_for_S = 2
Pepperoni_for_M_L=3
extra_cheese_cheese= 1
small_pizza=S+Pepperoni_for_S+extra_cheese_cheese
medium_pizza=M+Pepperoni_for_M_L+extra_cheese_cheese
large_pizza=L+Pepperoni_for_M_L+extra_cheese_cheese
 
if size=="S"and add_pepperoni=="Y" and extra_cheese=="Y" :
  print(f"Your final bill is: ${small_pizza}.")
elif size=="S" and add_pepperoni=="Y" and extra_cheese=="N":
    small_pizza-=extra_cheese_cheese
    print(f"Your final bill is: ${small_pizza}.")
elif size=="S" and add_pepperoni=="N" and extra_cheese=="Y":
    small_pizza-=Pepperoni_for_S
    print(f"Your final bill is: ${small_pizza}.")
elif size=="M" and add_pepperoni=="N" and extra_cheese=="N":
    print(f"Your final bill is: ${S}.")
# medium_pizza

elif  size=="M"and add_pepperoni=="Y" and extra_cheese=="Y" :
  print(f"Your final bill is: ${medium_pizza}.")
elif size=="M" and add_pepperoni=="Y" and extra_cheese=="N":
    medium_pizza-=extra_cheese_cheese
    print(f"Your final bill is: ${medium_pizza}.")
elif size=="M" and add_pepperoni=="N" and extra_cheese=="Y":
    medium_pizza-=Pepperoni_for_M_L
    print(f"Your final bill is: ${medium_pizza}.")
elif size=="M" and add_pepperoni=="N" and extra_cheese=="N":
    print(f"Your final bill is: ${M}.")

#large_pizza
    
elif  size=="L"and add_pepperoni=="Y" and extra_cheese=="Y" :
  print(f"Your final bill is: ${large_pizza}.")
elif size=="L" and add_pepperoni=="Y" and extra_cheese=="N":
    large_pizza-=extra_cheese_cheese
    print(f"Your final bill is: ${large_pizza}.")
elif size=="L" and add_pepperoni=="N" and extra_cheese=="Y":
    large_pizza-=Pepperoni_for_M_L
    print(f"Your final bill is: ${large_pizza}.")
elif size=="L" and add_pepperoni=="N" and extra_cheese=="N":
    print(f"Your final bill is: ${L}.")
else:
    print(f"Come back later.")



