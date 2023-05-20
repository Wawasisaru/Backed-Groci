class Customer:
    shop = "Groci_store"
    def __init__(self,name, email, order):
        self.name = name
        self.order = order
        self.email = email
        self.cart = []
    
  
    def place_order(self, order):
        self.order.append(order)
        print(f"Order placed successfully!")
        
    def cancel_order(self, order):
        if order in self.orders:
            self.orders.remove(order)
            print(f"Order cancelled successfully!")
        else:
            print(f"Order not found.")

