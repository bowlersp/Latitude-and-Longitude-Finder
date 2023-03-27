import requests

MY_LAT = 38.627003 # Your latitude
MY_LONG = -90.199402 # Your longitude

#WHERE IS THE ISS????
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(data)

#WHAT TIME IS SUNRISE AND SUNSET IN STL METRO AREA???

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 1,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = (data["results"]["sunrise"])
sunset = (data["results"]["sunset"])
day_length = (data["results"]["day_length"])
print(sunrise)
print(sunset)
print(f"The length of the day is {day_length}")
