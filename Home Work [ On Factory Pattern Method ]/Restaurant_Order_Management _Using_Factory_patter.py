from abc import ABC, abstractmethod


# Step 1: Create an interface for menu items
class MenuItem(ABC):
    @abstractmethod
    def serve(self):
        pass


# Step 2: Create concrete classes implementing the interface
class VegMeal(MenuItem):
    def serve(self):
        return "Serving a Veg Meal."


class NonVegMeal(MenuItem):
    def serve(self):
        return "Serving a Non-Veg Meal."


class Drink(MenuItem):
    def serve(self):
        return "Serving a Drink."


# Step 3: Create a Factory class to generate menu items
class MenuFactory:
    @staticmethod
    def get_item(item_type):
        if item_type.upper() == "VEGMEAL":
            return VegMeal()
        elif item_type.upper() == "NONVEGMEAL":
            return NonVegMeal()
        elif item_type.upper() == "DRINK":
            return Drink()
        else:
            return None


# Step 4: Use the Factory to get objects of concrete classes
class Restaurant:
    @staticmethod
    def main():
        menu_factory = MenuFactory()

        # Get a VegMeal and serve it
        item1 = menu_factory.get_item("VegMeal")
        print(item1.serve())

        # Get a NonVegMeal and serve it
        item2 = menu_factory.get_item("NonVegMeal")
        print(item2.serve())

        # Get a Drink and serve it
        item3 = menu_factory.get_item("Drink")
        print(item3.serve())


# Step 5: Verify the output
if __name__ == "__main__":
    Restaurant.main()
