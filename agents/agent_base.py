from abc import ABC, abstractmethod
from typing import Dict, List

class Agent(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def process_task(self, task: Dict) -> Dict:
        """Processes a given task and returns a result."""
        pass

    @abstractmethod
    def get_input_fields(self) -> List[str]:
        """Returns a list of input field names required for this agent."""
        pass
