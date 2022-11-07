##dictionary syntax

# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
# "Function": "A piece of code that you can easily call over and over again."}

##take items from the dictionary

# print(programming_dictionary["Bug"])

##Adding items in dictionary

# programming_dictionary["Loop"]= "To do something over and over."
# print(programming_dictionary)

##Create an empty dictionary

# empty_dictionary={}

##wipe the dictionary

# programming_dictionary={}
# print(programming_dictionary)

##edit an item in dictionary

# programming_dictionary["Bug"]="A insect in your computer."
# print(programming_dictionary)

##Loop through a dictionary

# for thing in programming_dictionary:
# 	print(thing)
# 	print(programming_dictionary[thing])
##########################
#nesting
# Capital={"France":"Paris","Germany":"Berlin",
# 	}
# #nesting a list in a dictionary
# travel_log={"Cities_visited":["paris", "lilly", "dijon"]
# 	}
#nesting a dictionary in a dictionary
# travel_log={"France":{"Cities_visited":["paris", "lilly", "dijon"] ,"Visited_places":12},
# "Germany":{"Cities_visited":["Berlin","Hamburg"], "Spend_time":"15 days", "capital":"Berlin"}
# }
# 
# print(travel_log)

#nesting a diction in a list
# travel_log=[
# {
# "Country":"France",
# "Cities_visited":["paris", "lilly", "dijon"],
# "Visited_places":12
# },
# {"Country":"Germany",
#  "Cities_visited":["Berlin","Hamburg"],
#  "Spend_time":"15 days",
#  "capital":"Berlin"
#  }
# ]
employees={}
for i in range (2):
	name=input("input your name: ")
	salary=int(input("input your salary: "))
	employees[name]=salary
for employee in employees:
	payment=employees[employee]
	if payment>salary:
		print("High salary.")
print(employees)