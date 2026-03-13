class Students:
    def __init__(self, student, price):
        self.student = student
        self.price = price

    def display(self):
        print(f"Sinh vien {self.student} co diem la  {self.price}")
h = Students("linhden", 8)
h.display()