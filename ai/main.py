import openai
import os
from typing import Optional
from functools import wraps

def handle_openai_error(func):
    """
    A decorator to handle OpenAI API errors gracefully.

    This decorator wraps a function that makes OpenAI API calls, catching
    any OpenAIError exceptions and returning their string representation.

    Args:
        func (callable): The function to be wrapped.

    Returns:
        callable: The wrapped function that includes error handling.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except openai.error.OpenAIError as e:
            return str(e)
    return wrapper

class ChatGPTHaikuGenerator:
    """
    Generate a haiku using GPT-3.5 Turbo
    """

    def __init__(self, api_key):
        """
        Initialize with the API key

        Args:
            api_key (str): OpenAI API Key for GPT-3.5 Turbo
        """
        self.api_key = api_key
        openai.api_key = self.api_key


def generate_haiku(api_key):
    """
    Generate a haiku using GPT-3.5 Turbo

    Args:
        api_key (str): The API key for OpenAI's GPT-3.5 Turbo

    Returns:
        str: The generated haiku
    """
    # Set the API key
    openai.api_key = api_key

    # Define the messages for the chat
    messages = [
        {"role": "system", "content": "You are a helpful assistant that generates haikus."},
        {"role": "user", "content": "Generate a haiku for me."}
    ]

    try:
        # Make the API call to generate the haiku
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Extract and return the haiku from the API response
        haiku = response['choices'][0]['message']['content']
        return haiku.strip()

    except openai.error.OpenAIError as e:
        return str(e)

# Replace with your new API key
api_key = "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"

# Generate and print the haiku
haiku = generate_haiku(api_key)
print("Generated Haiku:")
print(haiku)