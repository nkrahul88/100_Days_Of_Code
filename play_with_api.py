import requests
 
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
# print(data)

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

# iss_position = (latitude, longitude)

print(f"Latitude=, {latitude} , Longitude= {longitude} ")
