class Book:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_price(self):
        return self.price
    def set_price(self,price):
        self.price = price

book = Book("Alibaba", 10000)
print("Giá của sách:", book.get_price())