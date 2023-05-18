class Website: 
    def __init__(self, products, customers):
            self.products = products
            self.customers = 0 
    #displays information on products offered on the website   
    def display_info(self): 
       print(f"We offer {self.products} of various varieties") 
       
    
    #displays the number of new customers visiting the website
    def update_customers(self, count): 
        self.customers += count 
        print(f"{self.visitors} are the number of new customers who visited our website") 
    












