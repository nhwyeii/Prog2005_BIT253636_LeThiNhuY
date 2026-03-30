n = 1
tong = 0

while n <= 30:
    if n % 2 != 0:
        print(n)
        tong += n
    n += 1

print("Tổng các số lẻ:", tong)