import requests



API_KEY= "f97fb248f0cc0f24a4f540d399b0fa44"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


city = input ("Enter a city name:")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

if (requests.get(request_url)).status_code == 200:
    data = (requests.get(request_url)).json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"]-273, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")

else:
    print("An error occurred")