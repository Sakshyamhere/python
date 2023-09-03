#!/usr/bin/python3

import pyowm
import pyttsx3
engine = pyttsx3.init()
# from tkinter import *
# from tkinter import ttk

api_key = "d4d758dadd96926671d0e0d95563a968"
owm=pyowm.OWM(api_key)
weather_mgr = owm.weather_manager()
place = input('Enter Place Name: ')

# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()

# label=ttk.Label(frm, text="Kun thau ko?").grid(column=0, row=0)
# entry1 = ttk.Entry(root).grid(column=0, row=1)

# def bingus():
#     label.destroy()
#     btn.destroy()

    # ttk.Label(frm, text=f'Humidity: {humidity}%').grid(column=0, row=2)
# ttk.Label(frm, text=f'Wind Speed: {wind}m/s').grid(column=0, row=3)
#     entry1.destroy()

# btn=ttk.Button(frm, text="Search", command=bingus).grid(column=2, row=2)
# root.mainloop()





observation = weather_mgr.weather_at_place(place)
temperature = observation.weather.temperature("celsius")["temp"]
humidity = observation.weather.humidity
wind = observation.weather.wind()
status = observation.weather.detailed_status


print(f'Status: {status}')
print(f'Temperature: {temperature}°C')
print(f'Humidity: {humidity}%')
print(f'Wind Speed: {wind["speed"]} m/s')


engine = pyttsx3.init()
engine.say(f" place {place} ,weather status in {place}{status},Temperature in {place}{temperature}°Celcius ,Humidity in {place} {humidity}% , Wind Speed in {place}{wind['speed']} meter per second")
engine.runAndWait()