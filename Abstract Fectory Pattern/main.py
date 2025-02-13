from england_factory import EnglandFactory
from spain_factory import SpainFactory

# Client
def main():
    factory = EnglandFactory()
    language = factory.create_language()
    capital_city = factory.create_capital()

    print(f"Language : {language.__class__.__name__}")
    print(f"Greet: {language.great()}")

    print(f"Capital: {capital_city.__class__.__name__}")
    print(f"Total Population: {capital_city.get_population()}")
    print(f"Top Attraction: {capital_city.list_top_attractions()}")



#To make sure This Main mehtod gets called on the start up here

if __name__ == "__main__":
    main()