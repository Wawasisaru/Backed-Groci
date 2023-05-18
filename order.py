class Order:
    # Attributes
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []
    

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found in order.")
# this method calculates the discount of the total amout
    def calculate_discounted_amount(self, discount_percentage):
        return f"{self.total_amount - (self.total_amount * discount_percentage / 100)}"