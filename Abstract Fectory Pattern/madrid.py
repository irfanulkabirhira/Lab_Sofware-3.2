from capital_city import CapitalCity


# Concrete Product for B1
class Madrid(CapitalCity):
    def get_population(self) -> int:
        return 32000000

    def list_top_attractions(self) -> []:
        return ["Royal Palace", "Prado Museum", "Retiro Park"]

