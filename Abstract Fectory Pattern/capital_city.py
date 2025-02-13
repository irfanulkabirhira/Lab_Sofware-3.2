from abc import ABC, abstractmethod

# Abstract productB
class CapitalCity(ABC):
    @abstractmethod
    def get_population(self) -> int:
        pass
    @abstractmethod
    def list_top_attractions(self) -> []:
        pass

