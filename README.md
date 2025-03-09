# Weather Api with Deepseek </h1>

<p>Data retrieved from <a href="https://www.visualcrossing.com/weather-api">Weather API</a></p>
<p>Generates advice or a date with help of DeepSeek R1 according to weather</p>
<p>Possible to retrieve such data:</p>
<ul>
    <li>Current weather</li>
    <li>Past weather of a day or a period of days</li>
    <li>Future weather of a day or a period of days</li>
</ul>

<p>Implemented GET request "/api/v1/answer"</p>
<p>Data should be given in such raw json:</p>

> { <br>
> "token": token, <br>
> "requester_name": requester_name, <br>
> "location": location, <br>
> "date": date, <br>
> }

<p>Answer given in such format:</p>

> { <br>
> "advice": DeepSeek advice, <br>
> "requester_name": requester_name, <br>
> "timestamp": datetime.UTC, <br>
> "location": location, <br>
> "date": date, <br>
> "weather": Weather <br>
> }

<p>Weather class</p>

> { <br>
> "conditions": "Partially cloudy",<br>
> "description": "Clearing in the afternoon.",<br>
> "humidity": in %,<br>
> "pressure": in mb,<br>
> "temp": in Celsius,<br>
> "tempmax": in Celsius,<br>
> "tempmin": in Celsius,<br>
> "windspeed": in km/h<br>
> }