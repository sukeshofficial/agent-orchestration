
# 🤖 LLM-Powered Agent Orchestrator

This project is a lightweight agent orchestration system powered by **OpenRouter LLMs**. It automatically detects user intent (like weather, joke, or reminder) and routes the request to the appropriate smart agent — which then uses LLMs to generate intelligent responses.

---
![image](https://github.com/user-attachments/assets/e1086d60-8b79-455d-9b90-9cbae2bbc668)
<p align="center">
  <img src="https://github.com/user-attachments/assets/e1086d60-8b79-455d-9b90-9cbae2bbc668" 
       alt="Screenshot"  
       style="border-radius: 12px" />
</p>

---

## 🚀 Features

- 🔁 **Automatic Agent Routing** via OpenRouter (e.g., "Tell me a joke" → `JokeAgent`)
- 🧠 **LLM-powered Agents**: Each agent calls OpenRouter to process tasks naturally
- 💬 **Natural Language Input**: Just type what you want — no buttons, no commands
- 🧩 Modular agents with customizable prompts
- 📍 Location extraction from free-text (for WeatherAgent)

---

## 🧠 Supported Agents

| Agent          | Triggered By                                      | Output Example                                  |
|----------------|----------------------------------------------------|--------------------------------------------------|
| `JokeAgent`    | "Tell me a joke", "Make me laugh"                  | "Why do programmers prefer dark mode? Because light attracts bugs." |
| `WeatherAgent` | "What’s the weather in Mumbai?", "Is it hot today?"| "The weather in Mumbai is sunny and 32°C."      |
| `ReminderAgent`| "Remind me to call mom at 6 PM"                    | "Sure! I'll remind you to call mom at 6 PM."    |

---

## 🛠 Folder Structure

```
agent-orchestrator/
│
├── main_orchestrator.py        # 🧠 Entry point
├── llm_utils.py                # 🔌 OpenRouter API wrapper
├── .env                        # 🔑 Your OpenRouter API key
│
└── agents/
    ├── agent_base.py
    ├── joke_agent.py
    ├── weather_agent.py
    └── reminder_agent.py
```

---

## ⚙️ How It Works

1. **User types a request** in natural language (e.g., "What’s the weather in Chennai?")
2. `llm_utils.py` sends it to OpenRouter with a **classification prompt**
3. The response (`"weather"`) is used to **route to the right Agent**
4. That agent then sends another **LLM prompt to OpenRouter** to generate a full response

---

## 🧪 Examples

```
Enter your request: Tell me a programming joke

Agent call: Joke Agent
Result: Why do Java developers wear glasses? Because they don't C#.
```

```
Enter your request: Remind me to drink water at 5 PM

Agent call: Reminder Agent
Stored reminder: Sure! I've set a reminder for you to drink water at 5 PM.
```

```
Enter your request: What's the weather in Bangalore?

Agent call: Weather Agent
Weather update for Bangalore: It's mostly sunny with temperatures around 31°C.
```

---

## 🔧 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/agent-orchestrator.git
cd agent-orchestrator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup `.env`
Create a `.env` file in the root folder with your OpenRouter key:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 4. Run the App
```bash
python main_orchestrator.py
```

---

## 📦 Dependencies

- Python 3.10+
- `requests`
- `python-dotenv`
- OpenRouter API access

Install all at once:
```bash
pip install requests python-dotenv
```

---

## 🙏 Credits

Built with 💡 by Sukesh using OpenRouter + Python.

---

## 📄 License

MIT License
