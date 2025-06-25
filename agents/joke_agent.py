from agents.agent_base import Agent
from llm_utils import query_openrouter_task
from typing import Dict, List

class JokeAgent(Agent):
    def __init__(self, name: str = "JokeAgent"):
        super().__init__(name)

    def process_task(self, task: Dict) -> Dict:
        prompt = "Tell me a short and funny programming joke."
        result = query_openrouter_task(prompt)
        return {"result": f"\n{result.strip()}"}

    def get_input_fields(self) -> List[str]:
        return []
