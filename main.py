
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API Key
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Short-term memory settings
MEMORY_LIMIT = 10
chat_history = []


# Get user message
def get_user_message():
    return input("You: ")


# Save message in memory
def save_message(role, message):
    chat_history.append({
        "role": role,
        "content": message
    })


# Limit memory size
def limit_memory():

    while len(chat_history) > MEMORY_LIMIT:
        del chat_history[:2]


# Generate response using memory
def generate_response():

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=chat_history
    )

    return response.choices[0].message.content


# Manage conversation
def chat():

    print("AI Agent with Short-Term Memory Started!")
    print("Memory limit:", MEMORY_LIMIT, "messages")
    print("Type 'exit' to stop.\n")

    while True:

        message = get_user_message()

        if message.lower() == "exit":
            break

        # Save user message
        save_message("user", message)

        # Remove old messages if necessary
        limit_memory()

        # Generate AI response
        answer = generate_response()

        print("Agent:", answer)

        # Save AI response
        save_message("assistant", answer)

        # Limit memory again
        limit_memory()


# Main function
def main():
    chat()


if __name__ == "__main__":
    main()
