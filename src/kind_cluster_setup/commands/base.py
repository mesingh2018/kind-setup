from abc import ABC, abstractmethod
import argparse

class Command(ABC):
    @abstractmethod
    def execute(self, args: argparse.Namespace) -> None:
        """Execute the command."""
        pass
