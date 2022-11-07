number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
import random
from art import logo
print(logo)
the_number=random.choice(number)
print(the_number)
user_input=input("The game has 3 difficulties. 'easy' , 'normal' and 'hard'. Which one you wanna play: ")

def number_position():
	user_choice=int(input("Guess a number: "))
	if user_choice<the_number:
		print("number is too low.")
	elif user_choice>the_number:
		print("number is too high.")
	elif user_choice>100 or user_choice<0:
		print("you input wrong number.")
	elif user_choice==the_number :
		return f"You win. Correct number is: {the_number}."


def easy():
	life=10
	game_end=False
	while game_end!=True and life!=0:
		if number_position()==f"You win. Correct number is: {the_number}.":
			print(f"You win. Correct number is: {the_number}.")
			game_end=True
		else:
			life-=1
			print(f"Your have {life} life left. ")
		if life==0:
			print(f"You Lose. The correct answer is {the_number}.")

def normal():
	life=5
	game_end=False
	while game_end!=True and life!=0:
		if number_position()==f"You win. Correct number is: {the_number}.":
			print(f"You win. Correct number is: {the_number}.")
			game_end=True
		else:
			life-=1
			print(f"Your have {life} life left. ")
		if life==0:
			print(f"You Lose. The correct answer is {the_number}.")

def Hard():
	life=3
	game_end=False
	while game_end!=True and life!=0:
		if number_position()==f"You win. Correct number is: {the_number}.":
			print(f"You win. Correct number is: {the_number}.")
			game_end=True
		else:
			life-=1
			print(f"Your have {life} life left. ")
		if life==0:
			print(f"You Lose. The correct answer is {the_number}.")

if user_input=="easy":
	print("You have 10 lives.")
	easy()
elif user_input=="normal":
	print("You have 5 lives.")
	normal()
elif user_input=="hard":
	print("You have 3 lives.")
	Hard()
else:
	print("Invalid input.")
