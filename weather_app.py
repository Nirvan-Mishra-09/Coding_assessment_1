import requests
import argparse
import pyfiglet
from simple_chalk import chalk
import os

# API Key for openWeatherMap
API_KEY = "d11527d6c03eb83da0f614ab92f5aa05"
# Base URL for openWeatherMap API
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Mapping of weather codes to weather icons
WEATHER_ICONS = {
    "01d": "☀️", "02d": "⛅️", "03d": "☁️", "04d": "☁️", "09d": "🌧", 
    "10d": "🌦", "11d": "⛈", "13d": "🌨", "50d": "🌫", 
    "01n": "🌙", "02n": "☁️", "03n": "☁️", "04n": "☁️", "09n": "🌧", 
    "10n": "🌦", "11n": "⛈", "13n": "🌨", "50n": "🌫",
}

FAVOURITES_FILE = "favourites.txt"

# Load favourites from file
def load_favourites():
    if os.path.exists(FAVOURITES_FILE):
        with open(FAVOURITES_FILE, "r") as file:
            return file.read().splitlines()
    return []

# Save favourites to file
def save_favourites(favourites):
    with open(FAVOURITES_FILE, "w") as file:
        for city in favourites:
            file.write(f"{city}\n")

# Add a city to favourites
def add_favourite(city):
    favourites = load_favourites()
    if len(favourites) >= 3:
        print(chalk.red("You can only add up to 3 favourite cities."))
        return
    favourites.append(city)
    save_favourites(favourites)
    print(chalk.green(f"{city} added to favourites!"))

# List all favourite cities
def list_favourites():
    favourites = load_favourites()
    if not favourites:
        print(chalk.yellow("You have no favourite cities added."))
        return

    print(chalk.cyan("Favourite Cities:"))
    for city in favourites:
        show_weather(city)

# Show weather for a specific city
def show_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        print(chalk.red(f"Error retrieving weather for {city}."))
        return

    data = response.json()
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    icon = data["weather"][0]["icon"]
    weather_icon = WEATHER_ICONS.get(icon, "")
    city_name = data["name"]
    country = data["sys"]["country"]
    
    output = f"{pyfiglet.figlet_format(city_name)}, {country}\n\n"
    output += f"{weather_icon} {description}\n"
    output += f"Temperature: {temperature}°C\n"
    output += f"Feels like: {feels_like}°C\n"
    
    print(chalk.green(output))

# Remove a city from favourites
def remove_favourite(city):
    favourites = load_favourites()
    if city in favourites:
        favourites.remove(city)
        save_favourites(favourites)
        print(chalk.green(f"{city} removed from favourites."))
    else:
        print(chalk.red(f"{city} is not in your favourites."))

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Check the weather for a certain country/city.")
parser.add_argument("action", choices=["add", "list", "remove", "show"], help="Action to perform (add, list, remove, show)")
parser.add_argument("city", nargs="?", help="City name for adding/removing/showing")
args = parser.parse_args()

if args.action == "add" and args.city:
    # Get weather information for the city and add to favourites
    show_weather(args.city)
    add_favourite(args.city)

elif args.action == "list":
    list_favourites()

elif args.action == "remove" and args.city:
    remove_favourite(args.city)

elif args.action == "show" and args.city:
    show_weather(args.city)
