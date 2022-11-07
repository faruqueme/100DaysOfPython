from art import logo, vs
from os import system, name

from projectData import data
import random



def player_1():
	first=int(choose_data1['follower_count'])
	return first

def player_2():
	scound=int(choose_data2['follower_count'])
	return scound



game_end=False 
i=0
while not game_end:
	print(logo,'\n')
	i+=1
	choose_data1=random.choice(data)
	
	choose_data2=random.choice([x for x in data if x != choose_data1])
	
# 	print(choose_data1['follower_count'])
# 	
# 	print(choose_data2['follower_count'])
	
	print(f"Compare A: {choose_data1['name']}, the {choose_data1['description']}, from {choose_data1['country']}.\n")
	
	print(vs,'\n')
	
	print(f"Compare B: {choose_data2['name']}, the {choose_data2['description']}, from {choose_data2['country']}.\n")
	user_choice=input("Who has more followers? Type 'A' or 'B': \n").lower()
	if user_choice=='a':
		if player_1()>player_2():
			print(f"You're right. Your current score is {i}.")
			
		else :
			print(f"You Lose! Your final score is {i-1}.")
			game_end=True 
	elif user_choice=='b':
		if player_1()<player_2():
			print(f"You're right. Your current score is {i}.")
			
		else :
			print(f"You Lose! Your final score is {i-1}.")
			game_end=True 



