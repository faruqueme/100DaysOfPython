travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
# russia_travel={}
# russia_travel["country"]="Russia"
# russia_travel["visits"]=2
# russia_travel["cities"]=["Moscow", "Saint Petersburg"]
# travel_log.append(russia_travel)

#########other proccess

# def add_new_country(country_visited, times_visited, places_visited):
# 	new_country={}
# 	new_country["country"]=country_visited
# 	new_country["visits"]=times_visited
# 	new_country["cities"]=places_visited
# 	travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
