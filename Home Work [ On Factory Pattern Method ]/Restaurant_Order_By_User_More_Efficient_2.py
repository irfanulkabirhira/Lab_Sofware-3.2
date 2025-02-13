''''

2️⃣ Convert the Factory Pattern into an Abstract Factory

    🔹 What's Changed?
    ✅ Abstract Factory (RestaurantFactory) replaces multiple factory classes.
    ✅ Supports multiple meal orders in a single request.
    ✅ Handles invalid meal types gracefully.
    ✅ Keeps the Factory Pattern structure intact.

Sample Example :
    Welcome to the Restaurant!
    Preparing Veg Meal: Grilled vegetables, rice, and salad.
    Serving VegMeal
    Enjoy your meal!

    Preparing Non-Veg Meal: Grilled chicken, mashed potatoes, and gravy.
    Serving NonVegMeal
    Preparing Drink: Fresh orange juice.
    Serving Drink
    Enjoy your meal!

    ❌ Invalid meal type: sushi
    Preparing Veg Meal: Grilled vegetables, rice, and salad.
    Serving VegMeal
    Preparing Drink: Fresh orange juice.
    Serving Drink
    Enjoy your meal!

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

# Step 3: Implement the Abstract Factory
class RestaurantFactory:
    @staticmethod
    def create_meal(meal_type):
        meal_classes = {"veg": VegMeal, "nonveg": NonVegMeal, "drink": Drink}
        meal_class = meal_classes.get(meal_type.lower())

        if meal_class:
            return meal_class()
        else:
            print(f"❌ Invalid meal type: {meal_type}")
            return None

# Step 4: Function to handle multiple orders
def order_meals(meal_types):
    meals = [RestaurantFactory.create_meal(meal) for meal in meal_types]
    meals = [meal for meal in meals if meal]  # Remove None values if an invalid meal is ordered

    for meal in meals:
        meal.prepare()
        meal.serve()

    if meals:
        print("Enjoy your meal!\n")

# Step 5: Simulate multiple orders
print("Welcome to the Restaurant!")

# Single order
order_meals(["veg"])

# Multiple orders
order_meals(["nonveg", "drink"])
order_meals(["veg", "drink", "sushi"])  # 'sushi' will be ignored as it's invalid
