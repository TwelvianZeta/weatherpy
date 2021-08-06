import unicodedata

import requests
import os

# Functions
def kToF(inputTemp):
    return (inputTemp-273.15) * 9/5 + 32
def newLine():
    return "\n"

#Check if api key exists
if(os.getenv("WEATHER_API_KEY") == None):
    print("Please create an account at http://openweathermap.org/api, create a key, and run 'setx WEATHER_API_KEY = ' your api key")
    exit(2)

version = "1.0-SNAPSHOT+build.1"

print("Version " + version)
r = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=08816,us&appid=" + os.getenv("WEATHER_API_KEY"))
print(r.json())
print(
    str(r.json()["name"]) + " " +
    "Temperature = " + str(kToF(r.json()["main"]["temp"])) + chr(8457) + newLine() +
    "ID " + str(r.json()["weather"][0]["id"]) + newLine() +
    "Weather today: " + str(r.json()["weather"][0]["description"]) + ", weather " + str(r.json()["weather"][0]["main"]).lower() + newLine()
)
