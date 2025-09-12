class Smartphone:
    def __init__(self, brand, color):
        self.brand = brand      # Attribute
        self.color = color      # Attribute
    
    def make_call(self, number):
        print(f"{self.brand} is calling {number}...")

    def send_message(self, number, message):
        print(f"{self.brand} sends '{message}' to {number}")

    def show_info(self):
        print(f"Smartphone: {self.brand}, Color: {self.color}")


# Inheritance
class Android(Smartphone):
    def __init__(self, brand, color, os_version):
        super().__init__(brand, color) 
        self.os_version = os_version   
    
    # Polymorphism
    def show_info(self):
        print(f"Android Phone: {self.brand}, Color: {self.color}, OS: {self.os_version}")


# Inheritance
class iPhone(Smartphone):
    def __init__(self, brand, color, ios_version):
        super().__init__(brand, color)
        self.ios_version = ios_version
    
    def show_info(self):
        print(f"iPhone: {self.brand}, Color: {self.color}, iOS: {self.ios_version}")


# Creating objects
phone1 = Smartphone("Techno", "Black")
phone2 = Android("Samsung", "Blue", "Android 14")
phone3 = iPhone("Apple", "White", "iOS 18")

# Using methods
phone1.show_info()
phone2.show_info()
phone3.show_info()

phone2.make_call("2658888859")
phone3.send_message("2658888859", "Hello from iPhone!")
