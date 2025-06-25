from agents.joke_agent import JokeAgent
from agents.weather_agent import WeatherAgent
from agents.reminder_agent import ReminderAgent
from agents.agent_base import Agent
from llm_utils import query_openrouter
from typing import Dict
import re

class Orchestrator:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}

    def register_agent(self, task_type: str, agent: Agent):
        self.agents[task_type] = agent

    def get_agent(self, task_type: str) -> Agent:
        return self.agents.get(task_type)

    def route_task(self, task: Dict) -> Dict:
        agent = self.get_agent(task.get("type"))
        if not agent:
            return {"result": f"No agent registered for task type: {task.get('type')}"}
        return agent.process_task(task)

def extract_location(user_input: str) -> str:
    match = re.search(r"\b(?:in|at)\s+([A-Za-z\s]+)", user_input, re.IGNORECASE)
    return match.group(1).strip() if match else "your location"

def main():
    orchestrator = Orchestrator()
    orchestrator.register_agent("joke", JokeAgent())
    orchestrator.register_agent("weather", WeatherAgent())
    orchestrator.register_agent("reminder", ReminderAgent())

    print("\n🤖 Welcome to the Real AI Agent Orchestrator!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter your request: ").strip()
        if user_input.lower() == "exit":
            print("👋 Exiting the orchestrator. Goodbye!")
            break

        task_type = query_openrouter(user_input).strip().lower()
        agent = orchestrator.get_agent(task_type)

        if not agent:
            print(f"❌ No agent found for task type: {task_type}\n")
            continue

        task = {"type": task_type}

        if task_type == "weather":
            location = extract_location(user_input)
            task["location"] = location

        for field in agent.get_input_fields():
            if field == "message" and task_type == "reminder":
                task["message"] = user_input
            elif field not in task:
                task[field] = input(f"Enter {field}: ").strip()


        result = orchestrator.route_task(task)

        if task_type == "joke":
            print("\nAgent call: Joke Agent")
            print("Result:", result["result"], "\n")
        elif task_type == "reminder":
            print("\nAgent call: Reminder Agent")
            print("Stored reminder:", result["result"], "\n")
        elif task_type == "weather":
            print(f"\nAgent call: Weather Agent")
            print(f"Weather update for {task['location']}: {result['result']}\n")

if __name__ == "__main__":
    main()
