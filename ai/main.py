import openai
import os
from typing import Optional



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
        self.api_key = api_key
        self.engine = engine
        openai.api_key = self.api_key

    def generate_haiku(self):
        """
        Makes an API call to generate a random haiku.

        Returns:
            str: The generated haiku.
        """
        prompt = "Generate a random haiku that makes sense"
        max_tokens = 30 # Limit the number of tokens for the generated text
        try:
            response = openai.Completion.create(prompt=prompt, max_tokens=max_tokens, engine=self.engine)
            haiku = response.choices[0].text.strip()
            return haiku
        except openai.RequestException as e:
            print(e)
            return str(e)

if __name__ == "__main__":
    openai.api_key = os.environ['api_key']
