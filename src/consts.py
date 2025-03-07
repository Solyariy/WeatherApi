import os

from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY=os.environ.get("WEATHER_API_KEY")
API_TOKEN=os.environ.get("API_TOKEN")