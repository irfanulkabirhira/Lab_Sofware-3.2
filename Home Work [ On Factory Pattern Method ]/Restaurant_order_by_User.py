from abc import ABC, abstractmethod

# Step 1: Define the base class for all meals
class Meal(ABC):
    @abstractmethod
    def prepare(self):
        pass

    def serve(self):
        print(f"Serving {self.__class__.__name__}")

# Step 2: Define concrete meal classes
class VegMeal(Meal):
    def prepare(self):
        print("Preparing Veg Meal: Grilled vegetables, rice, and salad.")

class NonVegMeal(Meal):
    def prepare(self):
        print("Preparing Non-Veg Meal: Grilled chicken, mashed potatoes, and gravy.")

class Drink(Meal):
    def prepare(self):
        print("Preparing Drink: Fresh orange juice.")

# Step 3: Define the abstract factory class
class MealFactory(ABC):
    @abstractmethod
    def create_meal(self):
        pass

# Step 4: Define concrete factory classes for each meal type
class VegMealFactory(MealFactory):
    def create_meal(self):
        return VegMeal()

class NonVegMealFactory(MealFactory):
    def create_meal(self):
        return NonVegMeal()

class DrinkFactory(MealFactory):
    def create_meal(self):
        return Drink()

# Step 5: Simulate the order management system
def order_meal(factory: MealFactory):
    meal = factory.create_meal()
    meal.prepare()
    meal.serve()
    print("Enjoy your meal!")

# Step 6: Run the order system
if __name__ == "__main__":
    print("Welcome to the Restaurant!")
    print("Menu:")
    print("1. VegMeal")
    print("2. NonVegMeal")
    print("3. Drink")

    # Get user input
    choice = input("Enter the number of the meal you want to order: ").strip()

    # Use the appropriate factory based on user input
    if choice == "1":
        order_meal(VegMealFactory())
    elif choice == "2":
        order_meal(NonVegMealFactory())
    elif choice == "3":
        order_meal(DrinkFactory())
    else:
        print("Invalid choice. Please try again letter.")