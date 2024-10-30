import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def get_weather_data():
    """
    Example using the Gemini API with an API key.
    """
    try:
        headers = {
            'Authorization': f'Bearer {GEMINI_API_KEY}'
        }
        
        # Example Gemini API request
        response = requests.get("https://api.gemini.com/v1/weather", headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to get weather data"}
    except Exception as e:
        return {"error": str(e)}
