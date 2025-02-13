from abc import ABC, abstractmethod
from language import Language
from capital_city import CapitalCity

# AbstractFactory
class InternationalFactory(ABC):
    @abstractmethod
    def create_language(self) -> Language:
        pass
    @abstractmethod
    def create_capital(self) -> CapitalCity:
        pass
