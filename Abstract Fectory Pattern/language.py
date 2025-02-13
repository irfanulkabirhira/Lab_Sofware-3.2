from abc import ABC, abstractmethod


# Abstract ProductA
class Language(ABC):
    @abstractmethod
    def great(self):
        pass
