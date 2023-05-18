class Website:
    def __init__(self, name, url):
        self.name = name
        self.url = url

        #this method returns the name of the website
    def get_name(self):
        return f"{self.name}"
    
        #this method returns the url of the website|
    def get_url(self):
        return f"{self.url}"
    
        #this method takes a new url as input
    def set_url(self, new_url):
        self.url = new_url
        return f"{self.url}"
    
        #prints the name of the url of the website
    def print_details(self):
        print(f"{self.name}")
        print(f"{self.url}")











