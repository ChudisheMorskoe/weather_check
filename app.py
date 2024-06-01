from dotenv import load_dotenv
import os
import tkinter as tk
import requests


def get_weather(city):

    load_dotenv()
    api_key = os.getenv('API_KEY')

    base_url = "http://api.weatherapi.com/v1/current.json"
    complete_url = f"{base_url}?key={api_key}&q={city}&aqi=no"

    response = requests.get(complete_url)
    return response.json()


def show_weather():
    city = city_entry.get()  # take a city from input
    weather_data = get_weather(city)  # put city and get weather

    if "error" not in weather_data:
        current = weather_data["current"]
        location = weather_data["location"]

        temperature = current["temp_c"]
        humidity = current["humidity"]
        weather_description = current["condition"]["text"]
        wind_speed = current["wind_kph"]

        # make information about weather
        weather_info = f"Country: {location['name']}, {location['country']}\n" \
                       f"Temperature: {temperature}°C\n" \
                       f"Humidity: {humidity}%\n" \
                       f"Description: {weather_description}\n" \
                       f"Wind speed: {wind_speed} km/h"

        weather_label.config(text=weather_info)
    else:
        weather_label.config(text="City not found!")


root = tk.Tk()
root.title("Weather")
city_entry = tk.Entry(root, width=50)
city_entry.pack(padx=20, pady=10)
get_weather_button = tk.Button(root, text="Get the weather", command=show_weather)
get_weather_button.pack(pady=10)
weather_label = tk.Label(root, text="", font=("Helvetica", 14))
weather_label.pack(pady=10)
root.mainloop()
