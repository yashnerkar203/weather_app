
import tkinter as tk
import requests

# OpenWeatherMap API endpoint and API key
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "a926af24945c50245d011e2ba60de26c"

def get_weather(city):
    # Make a request to the OpenWeatherMap API
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(API_ENDPOINT, params=params)
    weather_data = response.json()

    # Extract relevant weather information from the API response
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]

    # Update the weather information in the GUI
    temperature_label.config(text=f"Temperature: {temperature}°C", fg="white", bg="#3e65e9")
    description_label.config(text=f"Description: {description}", fg="white", bg="#3e65e9")

# Create the main window
window = tk.Tk()
window.title("Weather App by Yash Nerkar")
window.geometry("400x200")
window.configure(bg="#3e65e9")  # Set background color

# Create GUI elements with customized styling
city_entry = tk.Entry(window, font=("Arial", 15), width=20)
city_entry.pack(pady=10)

search_button = tk.Button(window, text="Search", command=lambda: get_weather(city_entry.get()), bg="#f39c12", fg="white", font=("Arial", 12))
search_button.pack()

temperature_label = tk.Label(window, text="", bg="#3e65e9", fg="white", font=("Arial", 12, "bold"))
temperature_label.pack(pady=10)

description_label = tk.Label(window, text="", bg="#3e65e9", fg="white", font=("Arial", 12, "italic"))
description_label.pack()

# Start the main event loop
window.mainloop()
