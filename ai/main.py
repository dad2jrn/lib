import openai
import os
from typing import Optional
from functools import wraps

def handle_openai_error(func) -> Optional[str]:
    """
    A decorator to handle OpenAI API errors gracefully.

    This decorator wraps a function that makes OpenAI API calls, catching
    any OpenAIError exceptions and returning their string representation.

    Args:
        func (callable): The function to be wrapped.

    Returns:
        Optional[str]: The string representation of an OpenAIError, if one occurs,
                       or None if the function succeeds without raising an exception.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Optional[str]:
        try:
            return func(*args, **kwargs)
        except openai.error.OpenAIError as e:
            return str(e)
    return wrapper

class ChatGPTHaikuGenerator:
    """
    Generate a haiku using GPT-3.5 Turbo
    """

    def __init__(self, api_key: str) -> None:
        """
        Initialize with the API key

        Args:
            api_key (str): OpenAI API Key for GPT-3.5 Turbo
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    @handle_openai_error
    def generate_haiku(self) -> Optional[str]:
        """
        Generate a haiku using GPT-3.5 Turbo

        Returns:
            Optional[str]: The generated haiku as a string or None if generation fails.
        """
        # Define the messages for the chat
        messages = [
            {"role": "system", "content": "You are a helpful assistant that generates haikus."},
            {"role": "user", "content": "Generate a haiku for me."}
        ]

        # Make the API call to generate the haiku
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Extract and return the haiku from the API response
        haiku = response['choices'][0]['message']['content']
        return haiku.strip()

if __name__ == "__main__":
    api_key = os.environ.get("api_key")
    haiku_generator = ChatGPTHaikuGenerator(api_key)
    haiku = haiku_generator.generate_haiku()
    print("Generated Haiku: ")
    print(haiku)
