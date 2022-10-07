travel_log = [
{
    "country" : "India",
    "cities" : ["Bangalore", "patna", "pune"],
    "times": 10
},

{
    "country" : "United kingdom",
    "cities" : ["London", "Miltonkeys", "Brighton"],
    "times": 1,
},
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_dict = {}
    new_dict["country"] = country_visited
    new_dict["times"] = times_visited
    new_dict["cities"] = cities_visited
    travel_log.append(new_dict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
