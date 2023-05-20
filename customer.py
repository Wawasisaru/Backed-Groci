class Customer:
    shop = "Groci_store"
    def __init__(self,name, email, transaction,loyalty_points):
        self.name = name
        self.email = email
        self.transaction = transaction
        self.loyalty_points = loyalty_points
        self.cart = []
    
    def add_to_cart(self,item):
        self.cart.append(item)
        print(f"{self.cart}")


    def remove_from_cart(self,item):
        if item in self.cart:
            self.cart.remove(item)
        print(f"{self.cart}")


    def get_transaction(self):
        print (f"Trasaction, {self.name}  {self.transaction} {self.email}")


    def add_points(self):
        print(f"Thank you for shopping with Groci store, you have received {self.loyalty_points} points")
        


# customer1 = Customer(name = "sheila", email = "sheila@gmai.com", transaction = 20000, loyalty_points = 92)
# >>> customer1.add_to_cart("banana")
# ['banana']

# customer1 = Customer(name = "sheila", email = "sheila@gmai.com", transaction = 20000, loyalty_points = 92)
# >>> customer1.remove_from_cart("apple")
# []

# customer1 = Customer(name = "sheila", email = "sheila@gmai.com", transaction = 20000, loyalty_points = 92)
# >>> customer1.get_transaction()
# Trasaction, sheila  20000 sheila@gmai.com

# customer1 = Customer(name = "sheila", email = "sheila@gmai.com", transaction = 20000, loyalty_points = 92)
# >>> customer1.add_points()
# Thank you for shopping with Groci store, you have received 92 points
