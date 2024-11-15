# Weather CLI App 🌤️

A command-line weather application that allows users to check weather conditions for any city, manage favorite locations, and display weather information with beautiful ASCII art and emoji icons.

## Features ✨

- Check current weather conditions for any city
- Save up to 3 favorite cities for quick access
- Beautiful ASCII art city names using Pyfiglet
- Colorful terminal output with Chalk
- Weather condition emojis
- Temperature in Celsius
- "Feels like" temperature data
- Weather descriptions
- Country code display

## Prerequisites 📋

Before running the application, make sure you have Python installed and the following packages:

```bash
pip install requests pyfiglet simple-chalk argparse
```

## Usage💻

1) show cmd
   
![show](https://github.com/user-attachments/assets/83d5dd39-bcde-4bc0-9ca8-4eca2ca7a688)

2) remove cmd
  
![remove](https://github.com/user-attachments/assets/f51b7b9e-7bea-4df2-9870-560d410d16f1)

3) add cmd

![add](https://github.com/user-attachments/assets/15690840-3029-4d99-b2b0-117fac0d9b92)

4) list cmd
   
![fav](https://github.com/user-attachments/assets/79d48afc-b1ba-442f-bc77-5c966c598a2e)


## Weather Icons 🎨
The application displays different weather icons based on conditions:

- ☀️ Clear sky (day)
- 🌙 Clear sky (night)
- ⛅️ Few clouds (day)
- ☁️ Cloudy
- 🌧 Rain
- 🌦 Rain with sun
- ⛈ Thunderstorm
- 🌨 Snow
- 🌫 Mist

## Technical Details 🔧

- Uses OpenWeatherMap API for weather data
- Stores favorites in a local text file (favourites.txt)
- Temperatures are displayed in Celsius
- Maximum of 3 favorite cities can be stored

