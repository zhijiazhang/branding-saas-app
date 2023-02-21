import os
import openai
from dotenv import load_dotenv

load_dotenv() #load files from .env file

thing = 'coffee'
prompt = f'Generate a catchy branding snippet for {thing}'
prompt2 = f'Generate a list audiences for my brand {thing}'
openai.api_key = os.getenv("OPENAI_APIKEY")

response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=24)

response2 = openai.Completion.create(engine="text-davinci-003", prompt=prompt2, max_tokens=32)

print(response2)
