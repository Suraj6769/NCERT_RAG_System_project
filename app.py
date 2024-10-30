from vector_db import query_vector_db
from utils import get_weather_data

class Agent:
    def __init__(self):
        self.greeting_keywords = ['hello', 'hi', 'hey']
        self.weather_keywords = ['weather', 'temperature']

    def decide_action(self, user_query):
        """
        Determines the action to take based on the user query.
        Either call VectorDB or perform another action like fetching weather data.
        """
        # Convert to lowercase for easier comparison
        query_lower = user_query.lower()

        # Check for greeting
        if any(keyword in query_lower for keyword in self.greeting_keywords):
            return "greeting", None

        # Check for weather request
        if any(keyword in query_lower for keyword in self.weather_keywords):
            weather_data = get_weather_data()
            return "weather", weather_data

        # Default action: call VectorDB if no other match
        vector_result = query_vector_db(user_query)
        return "vector_db", vector_result
