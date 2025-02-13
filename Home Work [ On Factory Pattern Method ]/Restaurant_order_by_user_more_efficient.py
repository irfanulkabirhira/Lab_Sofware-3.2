''''
1️⃣ Modify the Factory Pattern to Support Multiple Orders
== > Exsample :
    Welcome to the Restaurant!
    Menu:
    1. VegMeal
    2. NonVegMeal
    3. Drink
    4. Multiple Orders
    Enter your choice (1/2/3/4): 4

    Preparing Veg Meal: Grilled vegetables, rice, and salad.
    Serving VegMeal
    Preparing Drink: Fresh orange juice.
    Serving Drink
    Preparing Non-Veg Meal: Grilled chicken, mashed potatoes, and gravy.
    Serving NonVegMeal
    Enjoy your meal!
    
    🎯 Why is This Better?

    ✅ Allows batch ordering (multiple meals at once).
    ✅ More scalable and efficient for future extensions.
    ✅ Improves user experience with flexible ordering options.

'''

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

# Step 5: Modify the order function to handle multiple meals
def order_meals(factory_list):
    """Allows ordering multiple meals at once."""
    meals = [factory.create_meal() for factory in factory_list]  # Create meals
    for meal in meals:
        meal.prepare()
        meal.serve()
    print("Enjoy your meal!\n")

# Step 6: Simulate multiple orders
if __name__ == "__main__":
    print("Welcome to the Restaurant!")
    print("Menu:")
    print("1. VegMeal")
    print("2. NonVegMeal")
    print("3. Drink")
    print("4. Multiple Orders")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "1":
        order_meals([VegMealFactory()])
    elif choice == "2":
        order_meals([NonVegMealFactory()])
    elif choice == "3":
        order_meals([DrinkFactory()])
    elif choice == "4":
        order_meals([VegMealFactory(), DrinkFactory(), NonVegMealFactory()])
    else:
        print("Invalid choice. Please try again later.")
