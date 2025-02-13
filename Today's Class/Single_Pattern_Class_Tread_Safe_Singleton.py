'''
4️⃣ Implement a Thread-Safe Singleton
Updated RestaurantKitchen with Thread-Safe Singleton:

    =>Use the Lock: The Lock ensures that only one thread can execute the critical section of the code at a time,
           thus avoiding multiple instances being created in a multithreaded environment.
    =>Lock the instantiation: We ensure that the lock is applied only when the singleton instance is being created,
           so the rest of the code remains unaffected by the lock.

Summary:

     => Thread-Safe Singleton ensures that only one instance of a class is created,
     even when multiple threads are involved,avoiding issues like race conditions and conflicts.

     =>It is used when you want to control access to a shared resource in a multithreaded environment,
    ensuring consistency and efficiency.
'''
import threading

class RestaurantKitchen:
    _instance = None
    _lock = threading.Lock()  # Ensure thread safety

    def __new__(cls):
        with cls._lock:  # Locking to prevent race conditions
            if cls._instance is None:
                print("Initializing the Restaurant Kitchen...")
                cls._instance = super(RestaurantKitchen, cls).__new__(cls)
                cls._instance.orders = []
                cls._instance.menu = ["Pizza", "Burger", "Pasta", "Salad"]
        return cls._instance

    def place_orders(self, order):
        """Place an order if it exists in the menu"""
        if order in self.menu:
            self.orders.append(order)
            print(f"Order Received: {order}")
        else:
            print(f"❌ Order '{order}' is not available in the menu.")

    def show_orders(self):
        """Display all pending orders"""
        print("Current Orders:", self.orders)


# Function to simulate multiple threads
def place_order_in_thread(order):
    kitchen = RestaurantKitchen()
    kitchen.place_orders(order)
    kitchen.show_orders()


# Testing thread safety by placing orders in different threads
thread1 = threading.Thread(target=place_order_in_thread, args=("Pizza",))
thread2 = threading.Thread(target=place_order_in_thread, args=("Burger",))
thread3 = threading.Thread(target=place_order_in_thread, args=("Salad",))

# Starting threads
thread1.start()
thread2.start()
thread3.start()

# Joining threads to wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()

# Checking if all threads were using the same instance
print(thread1.is_alive(), thread2.is_alive(), thread3.is_alive())
