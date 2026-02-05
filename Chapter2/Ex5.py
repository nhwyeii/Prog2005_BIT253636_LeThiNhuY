s = input("Nhập chuỗi: ")
ch = input("Nhập ký tự cần đếm: ")

count = 0
for c in s:
    if c == ch:
        count += 1

print("Số lần xuất hiện:", count)
