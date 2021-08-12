import requests
import os

# Functions
from Constants import *


def kToF(inputTemp):
    return round((inputTemp-273.15) * 9/5 + 32, 2)
def newLine():
    return "\n"
def space():
    return " "
def kToC(inputtemp):
    return round(inputtemp-273.15, 2)
def dot():
    return "."
def printData(r):
    print("Raw data:")
    print(r.json())
    print()
    print(
        str(r.json()["name"]) + " " +
        "Temperature = " + str(r.json()["main"]["temp"]) + "K " + str(kToF(r.json()["main"]["temp"])) + chr(
            8457) + " " + str(kToC(r.json()["main"]["temp"])) + chr(8451) + newLine() +
        "Feels like " + str(r.json()["main"]["feels_like"]) + "K " + str(kToF(r.json()["main"]["feels_like"])) + chr(
            8457) + " " + str(kToC(r.json()["main"]["feels_like"])) + chr(8451) + newLine() +
        "High " + str(r.json()["main"]["temp_max"]) + "K " + str(kToF(r.json()["main"]["temp_max"])) + chr(
            8457) + " " + str(kToC(r.json()["main"]["temp_max"])) + chr(8451) + newLine() +
        "Low " + str(r.json()["main"]["temp_min"]) + "K " + str(kToF(r.json()["main"]["temp_min"])) + chr(
            8457) + " " + str(kToC(r.json()["main"]["temp_min"])) + chr(8451) + newLine() +
        "ID " + str(r.json()["weather"][0]["id"]) + newLine() +

        "The weather now is " + str(r.json()["weather"][0]["description"]) + ", or " + str(r.json()["weather"][0]["main"]).lower() + dot() + newLine()
    )

#Check if api key exists
if(os.getenv("WEATHER_API_KEY") == None):
    print("Please create an account at http://openweathermap.org/api, create a key, and run 'setx WEATHER_API_KEY = ' your api key")
    exit(2)


def weathergetLongTerm(uszipcode):
    j = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=" + uszipcode + ",us&appid=" + os.getenv(
        "WEATHER_API_KEY")).json()
    lat = j["coord"]["lat"]
    lon = j["coord"]["lon"]
    s = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + lon + "&appid=" + os.getenv("WEATHER_API_KEY"))
    print(s.json())
# Main function
def weatherget(uszipcode):
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?zip="+uszipcode+",us&appid=" + os.getenv("WEATHER_API_KEY"))
    printData(r)

def weatherGetCity(location, country):
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + location + "," + country + "&appid=" + os.getenv("WEATHER_API_KEY"))
    printData(r)

def weatherCity(location):
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=" + location + "&appid=" + os.getenv("WEATHER_API_KEY"))
    printData(r)
def init():
    try:
        uszip = str(input("Input US ZIP code, if not just leave empty.\n"))
        weatherget(uszip)
        weathergetLongTerm(uszip)
        return
    except:
        print("External location detected!" + newLine())
        city = str(input("Input city name" + newLine()))
        try:
            weatherGetCity(city, str(input("country (optional)" + newLine())))
        except:
            weatherCity(city)

# Start of program
print(app_name + newLine() + "Version " + version)
init()

