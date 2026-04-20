import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather():
    api_key = os.getenv("WEATHER_API_KEY")
    city = "Stockton"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'main' not in data:
            return "Weather service is warming up, try again in a few minutes!"
        
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        return f"Current weather in Stockton: {description}, {temp}°F, feels like {feels_like}°F, humidity {humidity}%"
    
    except Exception as e:
        return "Sorry, I couldn't fetch the weather right now!"

if __name__ == "__main__":
    print(get_weather())