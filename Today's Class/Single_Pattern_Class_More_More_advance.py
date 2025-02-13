'''
    3️⃣ Modify Singleton to Limit Orders
    =>Change: Modify your Singleton RestaurantKitchen to allow only 5 active orders at a time.
    To add user input for ordering meals in your code, you can modify the order_meals function to accept user input
     dynamically. Here's how you can do it:

sample Example :
    Welcome to the Restaurant!
    Enter the meals you want to order (comma separated, e.g., 'veg, drink'): veg, nonveg, drink
    Preparing Veg Meal: Grilled vegetables, rice, and salad.
    Serving VegMeal
    Preparing Non-Veg Meal: Grilled chicken, mashed potatoes, and gravy.
    Serving NonVegMeal
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

# Step 5: Simulate multiple orders with user input
print("Welcome to the Restaurant!")

# Get user input
order_input = input("Enter the meals you want to order (comma separated, e.g., 'veg, drink'): ").strip()

# Split the input into a list and pass it to the order_meals function
meal_types = [meal.strip() for meal in order_input.split(",")]

# Place the order
order_meals(meal_types)
