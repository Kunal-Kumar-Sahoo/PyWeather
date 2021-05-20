import tkinter as tk
import requests
import time

def getWeatherInfo(window):
    city = textField.get()
    API = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=47b2c289288f3d0c362470798f52f9b6"
    jsonData = requests.get(API).json()
    weatherCondition = jsonData["weather"][0]["main"]
    temperature = int(jsonData["main"]["temp"] - 273.15)
    minTemperature = int(jsonData["main"]["temp_min"] - 273.15)
    maxTemperature = int(jsonData["main"]["temp_max"] - 273.15)
    pressure = jsonData["main"]["pressure"]
    humidity = jsonData["main"]["humidity"]
    windSpeed = jsonData["wind"]["speed"]
    sunrise = time.strftime("%H:%M%S", time.gmtime(jsonData["sys"]["sunrise"] + 6*60*60))
    sunset = time.strftime("%H:%M%S", time.gmtime(jsonData["sys"]["sunset"] + 6*60*60))

    finalInfo = weatherCondition + "\n" + str(temperature) + "°C"
    finalData = "\n" + "Maximum Temperature: " + str(maxTemperature) + "°C" + "\n" +"Minimum Temperature: " + str(minTemperature) +  "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(windSpeed) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

    label1.config(text=finalInfo)
    label2.config(text=finalData)


window = tk.Tk()
window.geometry("600x500")
window.title("PyWeather")

f = ("ubuntu", 15, "bold")
t = ("ubuntu", 35, "bold")

textField = tk.Entry(window, justify="center",font=t)
textField.pack(pady=20)
textField.focus()
textField.bind("<Return>", getWeatherInfo)

label1 = tk.Label(window, font=t)
label1.pack()
label2 = tk.Label(window, font=f)
label2.pack()

window.mainloop()
