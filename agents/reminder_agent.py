from agents.agent_base import Agent
from llm_utils import query_openrouter_task
from typing import Dict, List

class ReminderAgent(Agent):
    def __init__(self, name: str = "ReminderAgent"):
        super().__init__(name)
        self.reminders = []

    def process_task(self, task: Dict) -> Dict:
        message = task.get("message", "")
        if message:
            self.reminders.append(message)

        prompt = f"User wants to set a reminder: '{message}'. Confirm it politely and briefly."
        result = query_openrouter_task(prompt)
        return {"result": f"\n{result.strip()}"}

    def get_input_fields(self) -> List[str]:
        return ["message"]
