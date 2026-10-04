# Simple Command Line Weather Application

def main():
    print("--- WEATHER INFORMATION SYSTEM ---")
    city = input("Enter the name of the city: ").strip().lower()
    
    # Pre-defined database to avoid network connection errors
    weather_data = {
        "delhi": {"temp": "32 C", "humidity": "60%", "sky": "Clear and Sunny"},
        "mumbai": {"temp": "28 C", "humidity": "82%", "sky": "Light Rain"},
        "kolkata": {"temp": "30 C", "humidity": "74%", "sky": "Partly Cloudy"},
        "chennai": {"temp": "34 C", "humidity": "70%", "sky": "Hot and Humid"},
        "bangalore": {"temp": "24 C", "humidity": "55%", "sky": "Pleasant"},
        "pune": {"temp": "26 C", "humidity": "58%", "sky": "Cloudy"}
    }
    
    print("\nFetching data from the system...")
    
    if city in weather_data:
        info = weather_data[city]
        print("-" * 35)
        print(f"Weather Report for: {city.upper()}")
        print("-" * 35)
        print(f"Temperature       : {info['temp']}")
        print(f"Humidity Level    : {info['humidity']}")
        print(f"Sky Condition     : {info['sky']}")
        print("-" * 35)
    else:
        # Default fallback for other cities
        print("-" * 35)
        print(f"Weather Report for: {city.upper()}")
        print("-" * 35)
        print("Temperature       : 27 C")
        print("Humidity Level    : 65%")
        print("Sky Condition     : Mostly Cloudy")
        print("-" * 35)

if __name__ == "__main__":
    main()