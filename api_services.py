"""
ARIA API Services
Weather, News, and Calendar integrations
"""

import requests
from datetime import datetime
from config import (
    WEATHER_API_KEY, 
    NEWS_API_KEY, 
    WEATHER_API_URL, 
    NEWS_API_URL
)


def get_weather(city: str = "Stockton") -> str:
    """Get current weather for a city"""
    try:
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "imperial"  # Fahrenheit
        }
        
        response = requests.get(WEATHER_API_URL, params=params, timeout=10)
        data = response.json()
        
        if response.status_code == 200:
            temp = round(data["main"]["temp"])
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            
            return f"It's {temp} degrees Fahrenheit in {city} with {description}. Humidity is {humidity}%."
        else:
            return f"Sorry, I couldn't get the weather for {city}."
            
    except Exception as e:
        print(f"Weather API error: {e}")
        return "Sorry, I'm having trouble getting the weather right now."


def get_news(category: str = "technology", country: str = "us") -> str:
    """Get top news headlines"""
    try:
        params = {
            "apiKey": NEWS_API_KEY,
            "country": country,
            "category": category,
            "pageSize": 3
        }
        
        response = requests.get(NEWS_API_URL, params=params, timeout=10)
        data = response.json()
        
        if response.status_code == 200 and data.get("articles"):
            articles = data["articles"][:3]
            headlines = [f"{i+1}. {a['title']}" for i, a in enumerate(articles)]
            
            return "Here are the top headlines: " + " ".join(headlines)
        else:
            return "Sorry, I couldn't fetch the news right now."
            
    except Exception as e:
        print(f"News API error: {e}")
        return "Sorry, I'm having trouble getting the news."


def get_time() -> str:
    """Get current time"""
    now = datetime.now()
    return f"It's {now.strftime('%I:%M %p')} on {now.strftime('%A, %B %d')}."


def get_date() -> str:
    """Get current date"""
    now = datetime.now()
    return f"Today is {now.strftime('%A, %B %d, %Y')}."


# Test the APIs
if __name__ == "__main__":
    print("\n--- Testing APIs ---\n")
    
    print("Time:", get_time())
    print()
    
    print("Weather:", get_weather("Stockton"))
    print()
    
    print("News:", get_news())
