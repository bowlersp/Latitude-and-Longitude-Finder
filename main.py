import requests
from datetime import datetime, timezone

MY_LAT = 38.627003 # Your latitude
MY_LONG = -90.199402 # Your longitude

#WHERE IS THE ISS????
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# print(data)

#WHAT TIME IS SUNRISE AND SUNSET IN STL METRO AREA???

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
day_length = (data["results"]["day_length"])
print(f"The current sunrise in the STL Metro area is: {sunrise} UTC")
print(f"The current sunset in the STL Metro area is: {sunset} UTC")
# print(f"The length of the day is {day_length}")

time_now = datetime.now(timezone.utc)
print(f"The current time is: {time_now} UTC")
