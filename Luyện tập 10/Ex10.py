danh_sach =[]
for i in range(5):
    danh_sach.append(input(f"Nhập chuỗi thứ {i + 1}: "))

print(danh_sach)
n = len(danh_sach)
for i in range(n - 1):
    for j in range(n - i - 1):
        if len(danh_sach[j]) < len(danh_sach[j + 1]):
            danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]
            print(f"Bước {i}-{j}: {danh_sach}")

print(danh_sach)