import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

chuoi = input("Nhập chuỗi: ")

numbers = [int(x.strip()) for x in chuoi.split(";")]

so_chan = 0
so_am = 0
so_nguyen_to = 0
tong = 0

print("Các số:")

for num in numbers:
    print(num)

    if num % 2 == 0:
        so_chan += 1

    if num < 0:
        so_am += 1

    if is_prime(num):
        so_nguyen_to += 1

    tong += num

trung_binh = tong / len(numbers)

print("So chan:", so_chan)
print("So am:", so_am)
print("So nguyen to:", so_nguyen_to)
print("Trung binh:", trung_binh)
