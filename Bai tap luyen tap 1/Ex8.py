class Students:
    def __init__(self,price):
        if 0<=price<=10:
            self.price = price
        else:
            print('diem sinh vien khong hop le')
