from agents.agent_base import Agent
from llm_utils import query_openrouter_task
from typing import Dict, List

class WeatherAgent(Agent):
    def __init__(self, name: str = "WeatherAgent"):
        super().__init__(name)

    def process_task(self, task: Dict) -> Dict:
        location = task.get("location", "your area")
        prompt = (
            f"Provide a short, realistic weather report for {location}. "
            f"Include the current condition and temperature in Celsius."
        )
        result = query_openrouter_task(prompt)
        return {"result": f"\n{result.strip()}"}

    def get_input_fields(self) -> List[str]:
        return []
