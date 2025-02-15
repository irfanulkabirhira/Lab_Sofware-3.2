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
    # For Creating
class MealFactory(ABC):
    @abstractmethod
    def create_meal(self):
        pass
    # for Deleting
    @abstractmethod
    def delete_meal(self, meal):
        pass

# Step 4: Define concrete factory classes for each meal type
class VegMealFactory(MealFactory):
    def create_meal(self):
        return VegMeal()

    def delete_meal(self, meal):
        print(f"Deleting {meal.__class__.__name__}")

class NonVegMealFactory(MealFactory):
    def create_meal(self):
        return NonVegMeal()

    def delete_meal(self, meal):
        print(f"Deleting {meal.__class__.__name__}")

class DrinkFactory(MealFactory):
    def create_meal(self):
        return Drink()

    def delete_meal(self, meal):
        print(f"Deleting {meal.__class__.__name__}")

# Step 5: Simulate the order management system
def order_meal(factory: MealFactory):
    meal = factory.create_meal()
    meal.prepare()
    meal.serve()
    print("Enjoy your meal!")
    return meal

def delete_order(factory: MealFactory, meal):
    factory.delete_meal(meal)
    print("Meal has been removed.")

# Step 6: Run the order system
if __name__ == "__main__":
    print("Welcome to the Restaurant!")
    print("Menu:")
    print("1. VegMeal")
    print("2. NonVegMeal")
    print("3. Drink")

    choice = input("Enter the number of the meal you want to order: ").strip()

    meal = None
    factory = None

    if choice == "1":
        factory = VegMealFactory()
    elif choice == "2":
        factory = NonVegMealFactory()
    elif choice == "3":
        factory = DrinkFactory()
    else:
        print("Invalid choice. Please try again later.")

    if factory:
        meal = order_meal(factory)
        delete_choice = input("Do you want to delete the meal? (yes/no): ").strip().lower()
        if delete_choice == "yes":
            delete_order(factory, meal)
