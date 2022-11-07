from logo import logo
#add
def add(n1,n2):
	return n1+n2

#substruct
def substruct(n1,n2):
	return n1-n2

#multiply
def multiply(n1,n2):
	return n1*n2

#divide
def divide(n1,n2):
	return n1/n2

#dictionary
operations={
			"+":add,
			"-":substruct,
			"*":multiply,
			"/":divide
			}

 
def calculator():
	print(logo)
	number_1=float(input("Enter the first number: "))
	for keys in operations:
		print(keys)
	should_continue=True
	
	while should_continue:
		pick_up=input("Pick a operation from the line above: ")
		number_2=float(input("Enter the scound number: "))
		choice_symbol=operations[pick_up]
		answer=choice_symbol(number_1,number_2)
		print(f"{number_1} {pick_up} {number_2} = {answer}")
		again=input(f"Type 'y' to continue with {answer} or type 'b' to start new calculator or type 'n' to exit calculation: ")
		if again=='y':
			number_1=answer
		elif again=='b':
			should_continue=False
			calculator()
		else :
			should_continue=False
			print(f"Your final result is {answer}. Come back again.")
calculator()