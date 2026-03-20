
danh_sach = []
for i in range(5):
    s = input(f"Nhập chuỗi {i + 1}: ")
    danh_sach.append(s)

n = len(danh_sach)
print(danh_sach)

for i in range(n):
    for j in range(0, n - i - 1):
        if len(danh_sach[j]) < len(danh_sach[j + 1]):
            danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]
            print(f"Bước hoán đổi (i={i}, j={j}): {danh_sach}")

print(danh_sach)