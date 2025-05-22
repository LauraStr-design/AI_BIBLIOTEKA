
import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()  # take environment variables

#load enviroment variables from .env file
secret = os.getenv("SECRET")

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

#initialize the OpenAI client
# Note: The OpenAI client is initalized with the base URL and API key.

client = OpenAI(
    base_url=endpoint,
    api_key=secret,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Tell me a joke about Kaunas?",
        }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)
joke = response.choices[0].message.content

with open("joke.txt", "w") as file:
    file.write(joke) # type: ignore



print(response.choices[0].message.content)