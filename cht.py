import openai
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
    
openai.api_key = os.getenv('cht_api')


def chat(prompt):
    
    configure()
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=[{"role": "user", "content":prompt}])

    return response.choices[0].messages.content.strip()

if __name__ == "__main__":
    while True:
        users_input = input("You: ")
        if users_input.lower() in ["Q","q"]:
            break
        print("chat GPT: ", chat(users_input) )