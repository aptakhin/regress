from abc import ABC, abstractmethod

from regress.context import RegressContext


class UserInteraction(ABC):
    """Abstract interaction with user"""
    @abstractmethod
    def ask_canonize(self, context: RegressContext, exc: Exception) -> bool:
        """Asks user for canonization"""
        pass