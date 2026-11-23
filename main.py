
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API Key
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


# Get user message
def get_user_message():
    return input("You: ")


# Generate AI response
def generate_response(message):

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content


# Run Agent
def main():

    print("AI Agent Started!")
    print("Type 'exit' to stop.\n")

    while True:

        message = get_user_message()

        if message.lower() == "exit":
            break

        answer = generate_response(message)

        print("Agent:", answer)


if __name__ == "__main__":
    main()
