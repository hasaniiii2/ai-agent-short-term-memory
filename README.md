
# AI Agent with Short-Term Memory

A simple AI agent built with Python and OpenRouter API to demonstrate short-term conversational memory.

## Project Versions

### Version 1: Without Memory
- Receives user messages.
- Generates AI responses.
- Sends each message independently to the AI model.
- Does not store conversation history.

### Version 2: With Short-Term Memory
- Stores user messages and AI responses.
- Sends conversation history to the AI model.
- Keeps the last 10 messages.
- Automatically removes older messages when the memory limit is exceeded.
- Allows changing the memory capacity.

## Technologies

- Python
- OpenRouter API
- OpenAI Python SDK
- python-dotenv

## Installation

Install the required libraries:

```bash
pip install openai python-dotenv
```

## Configuration

Create a `.env` file in the project directory:

```env
OPENROUTER_API_KEY=your_api_key
```

Replace `your_api_key` with your OpenRouter API key.

## Run the Project

```bash
python main.py
```

## Memory Configuration

The memory capacity can be changed in `main.py`:

```python
MEMORY_LIMIT = 10
```

Examples:

| Memory Limit | Approximate Conversation Turns |
|---|---|
| 10 messages | 5 turns |
| 20 messages | 10 turns |
| 30 messages | 15 turns |
| 50 messages | 25 turns |

Increasing the memory limit allows the agent to access more previous messages, but it also increases token consumption.

## How Short-Term Memory Works

1. The user sends a message.
2. The message is stored in `chat_history`.
3. The conversation history is sent to the AI model.
4. The model generates a response.
5. The response is stored in memory.
6. Old messages are removed when the memory limit is exceeded.

## Important Notes

- Memory is stored temporarily in RAM.
- Conversation history is lost when the application stops.
- Each new program execution starts with an empty memory.
- The project does not use a database or permanent storage.

## Purpose

This project demonstrates the difference between an AI agent without memory and an AI agent with short-term conversational memory.
