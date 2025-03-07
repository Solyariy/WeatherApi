from pydantic import BaseModel
from datetime import datetime
from datetime import timezone, datetime


class WeatherGetRequest:
    def __init__(self, data: dict[str: str]):
        self.requester_name: str = data["requester_name"]
        self.location: str = data["location"]
        self.date: str = data["date"]
        self.date2: str = data.get("date2")

    def __dict__(self):
        res = {
            "requester_name": self.requester_name,
            "location": self.location,
            "date": self.date
        }
        if self.date2: res["date2"] = self.date2
        return res


class WeatherResponse(WeatherGetRequest):
    def __init__(self, data: dict[str: str], weather_dict: dict[str: str]):
        super().__init__(data)
        self.timestamp: str = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        self.weather: dict = weather_dict.get("days")[0]

    def __dict__(self):
        res = super().__dict__()
        res["timestamp"] = self.timestamp
        res["weather"] = self.weather
        return res

