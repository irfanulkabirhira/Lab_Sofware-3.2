from capital_city import CapitalCity

# Concrete Product for B1

class London(CapitalCity):
    def get_population(self) -> int:
        return 89000000

    def list_top_attractions(self) -> []:
        return ["Tower Bridge", "Buckingham Palace", "Big Ben"]

