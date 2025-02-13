'''

==>The Singleton Design Pattern Ensures
 a class has only one instance and provides
 a global point of access to it
 '''

'''
Why is it Singleton?

✅ It ensures only one instance of Restourankitcehn is created using __new__.
✅ Every time a new object is requested, it returns the same instance.
✅ The orders and manue lists are shared across all instances, proving it behaves as a singleton.
 
 '''

class RestaurantKitchen:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Initializing the Restaurant Kitchen...")
            cls._instance = super(RestaurantKitchen, cls).__new__(cls)
            cls._instance.orders = []
            cls._instance.menu = ["Pizza", "Burger", "Pasta", "Salad"]  # Menu items
        return cls._instance

    def place_orders(self, order):
        """ Place an order if it exists in the menu """
        if order in self.menu:
            self.orders.append(order)
            print(f"Order Received: {order}")
        else:
            print(f"❌ Order '{order}' is not available in the menu.")

    def show_orders(self):
        """ Display all pending orders """
        print("Current Orders:", self.orders)


# Creating two waiter objects taking orders
waiter1 = RestaurantKitchen()
waiter2 = RestaurantKitchen()

# Place orders using both waiter objects
waiter1.place_orders("Pasta")   # ✅ Available in menu
waiter2.place_orders("Pizza")   # ✅ Available in menu
waiter1.place_orders("Sushi")   # ❌ Not in menu

# Displaying orders - both waiters share the same kitchen instance
waiter1.show_orders()

# Check if both waiter objects refer to the same kitchen
print(waiter1 is waiter2)  # ✅ True (proves Singleton)

