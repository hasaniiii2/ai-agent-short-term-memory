
# AI Agent Without Memory

A simple AI agent built with Python and OpenRouter API.

## Features
- Receives user messages
- Generates AI responses
- Does not store conversation history
- Each message is sent independently to the AI model

## Technologies
- Python
- OpenRouter API
- OpenAI Python SDK

## Installation

Install dependencies:

```bash
pip install openai python-dotenv
```

Create a `.env` file and add your API key:

```env
OPENROUTER_API_KEY=your_api_key
```

## Run

```bash
python main.py
```

## Purpose

This project demonstrates how an AI agent works without short-term memory.
