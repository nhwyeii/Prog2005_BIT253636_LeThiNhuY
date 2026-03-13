import random

m = int(input())
n = int(input())

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 100))
    matrix.append(row)

print("Ma trận:")
for row in matrix:
    print(row)


r = int(input("Nhap hang muon xem: "))
print("Hàng", r, ":", matrix[r-1])


c = int(input("Nhap cot muon xem: "))
print("Cot", c, ":")

for i in range(m):
    print(matrix[i][c-1])


max_value = matrix[0][0]

for row in matrix:
    for x in row:
        if x > max_value:
            max_value = x

print("Gia tri lon nhat:", max_value)
