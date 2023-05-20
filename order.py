class Order:
    # Attributes
    def __init__(self, order_id, customer_name,discount_percentage,total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_amount = total_amount
        self.discount_percentage = discount_percentage
        self.items = []
    

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item
        return total
    
    def remove_item(self, item):
        if item in self.item:
            self.item.remove(item)
        else:
            print("Item not found in order.")
# this method calculates the discount of the total amout
    def calculate_discounted_amount(self, discount_percentage,total_amount):
        return f"{self.total_amount - (self.total_amount * discount_percentage / 100)}"
# order = Order(order_id=24, customer_name="Nelly", discount_percentage=5)
