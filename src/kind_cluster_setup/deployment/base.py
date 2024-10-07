from abc import ABC, abstractmethod
from typing import Dict

class DeploymentStrategy(ABC):
    @abstractmethod
    def deploy(self, app: str, app_config: Dict[str, any], env_config: Dict[str, any]) -> None:
        """Deploy an application."""
        pass

    @abstractmethod
    def check_status(self, app: str, env_config: Dict[str, any]) -> str:
        """Check the status of a deployed application."""
        pass
