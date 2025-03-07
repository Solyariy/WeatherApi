from src.consts import WEATHER_API_KEY
from src.models import WeatherGetRequest


class WeatherApi:
    def __init__(self, model: WeatherGetRequest):
        self.url_base = ("https://weather.visualcrossing.com/"
                         "VisualCrossingWebServices/rest/services/timeline")
        self.location = model.location
        self.date1 = model.date
        self.date2 = model.date2

    def __str__(self):
        return (
            f"{self.url_base}/{self.location}/{self.date1}"
            f"{'/' + self.date2.__str__() if self.date2 else ''}"
            f"?unitGroup=metric&include=days"
            f"&elements=tempmax,tempmin,temp,conditions,description,humidity,windspeed,pressure"
            f"&key={WEATHER_API_KEY}"
        )


if __name__ == "__main__":
    data = {
        "token": "TOKEN",
        "requester_name": "me",
        "location": "Kyiv,Ukraine",
        "date": "2025-02-01"
    }
    wreq = WeatherGetRequest(data)
    wapi = WeatherApi(wreq)

    print(wreq.__dict__(), wapi)
