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
    
    TASK_SYSTEM_PROMPT = """
                            You are an intelligent assistant in a multi-agent orchestration system.

                            You respond to direct user instructions routed by a controller agent. Based on the request you receive, respond appropriately using the following behavioral guidelines.

                            ---

                            🃏 If the user is asking for a joke:
                            - Tell a short and clever programming joke.
                            - Keep it 1-2 lines max.
                            - Make it funny and original if possible.
                            - Avoid overused jokes unless cleverly rephrased.

                            🌦 If the user is asking for the weather:
                            - Provide a simulated, realistic-sounding weather update.
                            - Include current temperature in Celsius, condition (e.g., sunny, rainy), and overall feeling (e.g., "hot", "pleasant").
                            - Assume current time and respond naturally.
                            - Use the city or location provided in the prompt.

                            ⏰ If the user is asking to set a reminder:
                            - Confirm the reminder politely and naturally.
                            - Do not reword their message too much — reflect it back in a friendly way.
                            - Make them feel reassured that it's noted or scheduled.
                            - Add light encouragement or politeness when possible.

                            ---

                            📝 General Rules:
                            - Always sound like a helpful, human-like assistant.
                            - Keep responses short, warm, and natural.
                            - Do not mention that you are an AI or a bot.
                            - Avoid generic or robotic answers.
                            - Do not repeat the instruction — respond to it.

                            ✅ Examples:

                            User: Tell me a programming joke  
                            You: Why do Python devs prefer dark mode? Because light attracts bugs.

                            User: What's the weather in Chennai?  
                            You: It's mostly sunny in Chennai today with a high around 32°C. A warm, breezy afternoon.

                            User: Remind me to study at 6 PM  
                            You: Got it! I'll remind you to study at 6 PM. You’ve got this!

                            Only respond to the user’s input — don't explain yourself.
                        """


    body = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user", "content": prompt,
                "role": "system", "content": TASK_SYSTEM_PROMPT             
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"
