class Product:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
       if price >0:
           self.price = price
       else:
           print("gia truyen vao > 0")

    def __str__(self):
        return f"Price:{self.price}"


