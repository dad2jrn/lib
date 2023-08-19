from typing import Optional, Any
import json
import requests

class WeatherApp:

    def __init__(self):
        pass

    def read_api_key(self) -> Optional[str]:
        """Reads the API key from the provided file.

        Returns:
        - The API key as a string if successful, or None otherwise.
        """
        with open(self.api_key_file, 'r') as f:
            return f.read().strip()

    def get_ip_location(self) -> Optional[str]:
        """
        Retrieves the IP location of the user.

        Returns:
        --------
        str or None:
            The IP address if the retrieval was successful; None otherwise.
        """
        try:
            response = requests.get("https://ipapi.co/json/")
            response.raise_for_status()
            return response.json().get("ip")
        except requests.RequestException:
            print("Failed to fetch IP location.")
            return None

    def get_weather_data(self, query: str) -> Optional[Any]:
        """
        Fetches the weather data for the specified query.

        Parameters:
        -----------
        query : str
            The location (either IP or ZIP) for which weather data is sought.

        Returns:
        --------
        dict or None:
            Weather data in JSON format if retrieval was successful; None otherwise.
        """
        base_url = "http://api.weatherapi.com/v1/current.json?"
        url = f"{base_url}key={self.api_key}&q={query}"

    def run(self):
        pass

if __name__ == "__main__":
    app = WeatherApp()
    app.run()
