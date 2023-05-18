
class Stock:
 def __init__(self, product, quantity):
     self.product = product
     self.quantity = quantity


 def generate_purchase_order(self):
       print(f"Added {self.quantity} kgs of {self.product}.")


 def check_stock_level(self,item):
     for item in self.quantity:
         if item > 2000:
             print("Stock is updated")
     else:
         print("Stock needs to be updated")