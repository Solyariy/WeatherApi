from datetime import timezone, datetime
from groq import Groq
from consts import MODEL_API_KEY


class WeatherGetRequest:
    def __init__(self, data: dict[str: str]):
        self.requester_name: str = data["requester_name"]
        self.location: str = data["location"]
        self.date: str = data["date"]
        self.date2: str = data.get("date2")

    def to_dict(self):
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
        self.advice = None

    def to_dict(self):
        res = super().to_dict()
        res["timestamp"] = self.timestamp
        res["weather"] = self.weather
        res["advice"] = self.advice
        return res

    def ask_model(self):
        client = Groq(api_key=MODEL_API_KEY)
        response = client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=[
                {"role": "system",
                 "content": "Analyze the weather data and give short and precise advice on where should I get"
                            "my girlfriend for a date, answer should be max 3 sentences"},
                {"role": "user",
                 "content": self.weather.__str__()}
            ],
            max_completion_tokens=1024,
            max_tokens=200,
            stream=False,
            stop=None
        )
        self.advice = response.choices[0].message.content
        client.close()


