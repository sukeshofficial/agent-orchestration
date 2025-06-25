import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "openai/gpt-4o-mini"

def query_openrouter(prompt: str) -> str:
    SYSTEM_PROMPT = """
You are a routing assistant in a multi-agent orchestration system.

Your job is to classify any user request into **one** of these three agent types:

- joke
- weather
- reminder

✅ Output Format:
Only return one word from the list above — no explanation, no punctuation.

📌 Rules:
- No emojis, symbols, or formatting.
- No phrases or extra words — just one valid keyword.

📚 Examples:
User: Tell me a programming joke  
You: joke

User: What's the weather in Mumbai today?  
You: weather

User: Remind me to call my sister at 6 PM  
You: reminder

User: Is it hot in Delhi?  
You: weather

If you are unsure, always choose the closest valid type.
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"


def query_openrouter_task(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"
