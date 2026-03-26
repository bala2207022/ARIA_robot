"""
ARIA Configuration
Loads API keys from environment variables
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GOOGLE_CALENDAR_API_KEY = os.getenv("GOOGLE_CALENDAR_API_KEY")

# API Endpoints
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"


def get_api_key(name: str) -> str | None:
    """Get API key by name"""
    keys = {
        "claude": CLAUDE_API_KEY,
        "weather": WEATHER_API_KEY,
        "news": NEWS_API_KEY,
        "google_calendar": GOOGLE_CALENDAR_API_KEY,
    }
    return keys.get(name.lower())


# Verify keys are loaded
if __name__ == "__main__":
    print("API Keys Status:")
    print(f"  Claude: {'✓' if CLAUDE_API_KEY else '✗'}")
    print(f"  Weather: {'✓' if WEATHER_API_KEY else '✗'}")
    print(f"  News: {'✓' if NEWS_API_KEY else '✗'}")
    print(f"  Google Calendar: {'✓' if GOOGLE_CALENDAR_API_KEY else '✗'}")
