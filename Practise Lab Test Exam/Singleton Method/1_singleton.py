class RestaurantKitchen:
    _instance = None  # Store the single instance of the kitchen-> protected (Encapsulaiton)

    def __new__(cls):
        if cls._instance is None:
            print("Initializing the restaurant kitchen...")
            cls._instance = super(RestaurantKitchen, cls).__new__(cls)
            cls._instance.orders = []  # Shared order list
            cls._instance.menu = []    # Shared menu list
        return cls._instance  # Return the single instance

    def place_order(self, order):
        """Adds a new order to the kitchen"""
        if order in self.menu:
            self.orders.append(order)
            print(f"Order received: {order}")
        else:
            print(f"Sorry, {order} is not available on the menu!")

    def show_orders(self):
        """Displays all pending orders"""
        print("Current Orders:", self.orders)

    def show_menu(self):
        """Displays the current menu"""
        print("Menu:", self.menu)

    def add_to_menu(self, dish):
        """Adds a new dish to the menu"""
        if dish not in self.menu:
            self.menu.append(dish)
            print(f"{dish} has been added to the menu.")
        else:
            print(f"{dish} is already on the menu.")

    def remove_from_menu(self, dish):
        """Removes a dish from the menu"""
        if dish in self.menu:
            self.menu.remove(dish)
            print(f"{dish} has been removed from the menu.")
        else:
            print(f"{dish} is not in the menu.")

# Creating two waiters taking orders
waiter1 = RestaurantKitchen()
waiter2 = RestaurantKitchen()
# Adding items to the menu
waiter1.add_to_menu("Pasta")
waiter1.add_to_menu("Pizza")
waiter1.add_to_menu("Burger")
waiter2.add_to_menu("Banana Milk Shake")
waiter2.add_to_menu("Nachos")
# Display the menu
waiter1.show_menu()
# Placing orders using both waiter objects
waiter1.place_order("Pasta")
waiter2.place_order("Pizza")
waiter2.place_order("Banana Milk Shake")
waiter1.place_order("Salad")  # Not on the menu, will be rejected

# Displaying orders - both waiters share the same kitchen instance
waiter2.show_orders()

# Checking if both waiter objects refer to the same kitchen instance
print(waiter1 == waiter2)  # True (Same instance)
# Changing the menu - removing a dish
waiter2.remove_from_menu("Rui")
waiter2.remove_from_menu("Nachos")
# Display the updated menu
waiter2.show_menu()

