class Customer:
    shop = "Groci_store"
    def __init__(self,name, email, order):
        self.name = name
        self.order = order
        self.email = email
        self.cart = []
    
  
    def place_order(self, order):
        self.orders.append(order)
        print("Order placed successfully!")
        
    def cancel_order(self, order):
        if order in self.orders:
            self.orders.remove(order)
            print("Order cancelled successfully!")
        else:
            print("Order not found.")

