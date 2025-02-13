'''
2️⃣ Convert the Factory Pattern into an Abstract Factory (But here You can take order from User )

    🔹 How This Works?
    ✅ Takes user input for ordering meals.
    ✅ Allows multiple meals using a comma-separated list (e.g., veg, drink).
    ✅ Handles invalid orders (e.g., pasta will be ignored).
    ✅ Lets the user order again using a loop.

Sample Example :
    🍽️ Welcome to the Restaurant! 🍽️
    Available meals: veg, nonveg, drink
    Enter your order (comma-separated): veg, drink

    Preparing Veg Meal: Grilled vegetables, rice, and salad.
    Serving VegMeal
    Preparing Drink: Fresh orange juice.
    Serving Drink
    Enjoy your meal! 🍽️

    Would you like to order again? (yes/no): yes

    🍽️ Welcome to the Restaurant! 🍽️
    Available meals: veg, nonveg, drink
    Enter your order (comma-separated): nonveg, sushi

    ❌ Invalid meal type: sushi
    Preparing Non-Veg Meal: Grilled chicken, mashed potatoes, and gravy.
    Serving NonVegMeal
    Enjoy your meal! 🍽️

    Would you like to order again? (yes/no): no
    Thank you for dining with us! 😊

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
def order_meals():
    print("\n🍽️ Welcome to the Restaurant! 🍽️")
    print("Available meals: veg, nonveg, drink")

    user_input = input("Enter your order (comma-separated): ").strip().lower()
    meal_types = [meal.strip() for meal in user_input.split(",")]

    meals = [RestaurantFactory.create_meal(meal) for meal in meal_types]
    meals = [meal for meal in meals if meal]  # Remove None values if an invalid meal is ordered

    for meal in meals:
        meal.prepare()
        meal.serve()

    if meals:
        print("Enjoy your meal! 🍽️\n")


# Step 5: Take orders from the user in a loop
while True:
    order_meals()
    another_order = input("Would you like to order again? (yes/no): ").strip().lower()
    if another_order != "yes":
        print("Thank you for dining with us! 😊")
        break
