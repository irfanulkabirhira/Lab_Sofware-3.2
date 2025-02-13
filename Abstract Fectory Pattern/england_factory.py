from international_factory import InternationalFactory
from english import English
from london import London
from capital_city import CapitalCity
from language import Language

# Concrete Factory 1
class EnglandFactory(InternationalFactory):
    def create_language(self) -> Language:
        return English()

    def create_capital(self) -> CapitalCity:
        return London()
