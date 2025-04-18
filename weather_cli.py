import requests

API_KEY = "bfe72b204479a07b9a4ae73e7554a501"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" 
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']} °C",
            "Feels Like": f"{data['main']['feels_like']} °C",
            "Humidity": f"{data['main']['humidity']}%",
            "Condition": data["weather"][0]["description"].title()
        }

        return weather
    elif response.status_code == 404:
        return "City not found. Please check the name."
    else:
        return f"Error: {response.status_code}"

def main():
    print("🌤️  Simple Weather CLI App 🌍\n")
    city = input("Enter a city name: ").strip()

    result = get_weather(city)

    if isinstance(result, dict):
        print("\n📍 Weather Information:\n")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(f"\n❌ {result}")

if __name__ == "__main__":
    main()
