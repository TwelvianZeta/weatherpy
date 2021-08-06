import requests
import os

# Functions
def kToF(inputTemp):
    return (inputTemp-273.15) * 9/5 + 32
def newLine():
    return "\n"
def space():
    return " "
def kToC(inputtemp):
    return inputtemp-273.15

#Check if api key exists
if(os.getenv("WEATHER_API_KEY") == None):
    print("Please create an account at http://openweathermap.org/api, create a key, and run 'setx WEATHER_API_KEY = ' your api key")
    exit(2)

version = "1.0+build.5"
phase = "SNAPSHOT"
app_name = "weatherpy"
print(app_name + "\nVersion " + version)

degree = 176
def dot():
    return "."

def weatherget(uszipcode):
    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?zip="+uszipcode+",us&appid=" + os.getenv("WEATHER_API_KEY"))
    print(r.json())
    print(
        str(r.json()["name"]) + " " +
        "Temperature = " + str(r.json()["main"]["temp"]) + "K " + str(kToF(r.json()["main"]["temp"])) + chr(8457) + " " + str(kToC(r.json()["main"]["temp"])) + chr(8451) + newLine() +
        "ID " + str(r.json()["weather"][0]["id"]) + newLine() +
        "Weather today: " + str(r.json()["weather"][0]["description"]) + ", weather is " + str(
            r.json()["weather"][0]["main"]).lower() + dot() + newLine()
    )


weatherget(str(input("Input US ZIP code (localization comming soon:tm:)\n")))