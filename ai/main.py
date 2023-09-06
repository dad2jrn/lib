import openai
import os
from typting import Optional



class ChatGPTHaikuGenerator:
    """
    A class to generate haikus using the ChatGPT API.

    Attributes:
        api_key (str): The API key for OpenAI's GPT-3.
        engine (str): The engine to use for text generation.

    Methods:
        generate_haiku: Makes an API call to generate a random haiku.
    """
    def __init__(self, api_key, engine='text-davinci-002') -> Optional[None]:
        """
        Initializes a new instance of the ChatGPTHaikuGenerator class.

        Args:
            api_key (str): The API key for OpenAI's GPT-3.
            engine (str): The engine to use for text generation. Defaults to 'text-davinci-002'.
        """
        pass

    def generate_haiku(self):
        """
        Makes an API call to generate a random haiku.

        Returns:
            str: The generated haiku.
        """
        pass

if __name__ == "__main__":
    openai.api_key = os.environ['API_KEY']
