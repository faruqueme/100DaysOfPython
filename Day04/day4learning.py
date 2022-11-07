#randomization: It means you gave command to select random things like character, integer, floating point numbers and so on
#For_information:https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

#ramdom_integer
# import random
# random_integer=random.randint(0, 12)
# print(random_integer)

#random_floating_point-random.uniform-> is used to choose a number between two ranges

# import random
# random_float=random.uniform(5.165641,5.633256)
# print(random_float)

#Lists-> if we print specific data from the list we simply write- print(Saudi_arabia_states[0,1,2,3,etc])

# Saudi_arabia_states=['Riyadh', 'Makkah' ,'Eastern' ,'Madinah' ,'Al Baha' ,'Al Jawf' ,'Northern Borders' ,'Qassim' ]
# print(Saudi_arabia_states[5])

#change the data in list

# Saudi_arabia_states[2]='western'
# print(Saudi_arabia_states)
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#  
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[0][1])
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
z=map
input_num=input("input any numbers: ")
my_list = list(map(int,str(input_num)))
print(my_list)
x=my_list[0]
y=my_list[1]


print(z[x][y])














	








