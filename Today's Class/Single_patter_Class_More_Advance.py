'''
    3️⃣ Modify Singleton to Limit Orders
=>Change: Modify your Singleton RestaurantKitchen to allow only 5 active orders at a time.

'''

class RestaurantKitchen:
    _instance = None
    MAX_ORDERS = 5  # Limit orders

    def __new__(cls):
        if cls._instance is None:
            print("Initializing the Restaurant Kitchen...")
            cls._instance = super(RestaurantKitchen, cls).__new__(cls)
            cls._instance.orders = []
            cls._instance.menu = ["Pizza", "Burger", "Pasta", "Salad"]
        return cls._instance

    def place_order(self, order):
        if len(self.orders) < self.MAX_ORDERS:
            if order in self.menu:
                self.orders.append(order)
                print(f"Order Received: {order}")
            else:
                print(f"❌ Order '{order}' is not available in the menu.")
        else:
            print("⚠️ Kitchen at full capacity! Cannot take more orders.")

# Testing the modified Singleton
kitchen = RestaurantKitchen()
for _ in range(6):  # Trying to place 6 orders
    kitchen.place_order("Pizza")

print("Current Orders:", kitchen.orders)  # Should have max 5 orders
