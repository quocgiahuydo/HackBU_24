import openai

openai.api_key = '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'

def chat(prompt):

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=[{"role": "user", "content":prompt}])

    return response.choices[0].messages.content.strip()

if __name__ == "__main__":
    while True:
        users_input = input("You: ")
        if users_input.lower() in ["Q","q"]:
            break
        print("chat GPT: ", chat(users_input) )
        