pip install requests
import requests

def get_weather(city_name, api_key):
    # OpenWeatherMap API URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API call
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # 'metric' for Celsius, use 'imperial' for Fahrenheit
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract the main weather details
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        # Display the weather information
        print(f"Weather in {city_name.capitalize()}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Weather: {weather['description'].capitalize()}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        # Handle errors
        print(f"Error: Could not fetch weather data for {city_name}. Please check the city name or try again later.")

# Example usage
if __name__ == "__main__":
    # Input your OpenWeatherMap API key here
    api_key = "your_openweathermap_api_key"
    
    # Input the city name
    city_name = input("Enter the city name: ")

    # Fetch and display weather data
    get_weather(city_name, api_key)
