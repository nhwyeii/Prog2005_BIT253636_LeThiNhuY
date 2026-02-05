n = int(input("Nhập số: "))
s = 0

while n > 0:
    s += n % 10
    n //= 10

print("Tổng chữ số:", s)
