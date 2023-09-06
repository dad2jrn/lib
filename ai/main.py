import openai

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