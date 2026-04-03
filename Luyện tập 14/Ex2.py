danh_sach = []
for i in range(5):
    name = input(f"Nhập tên người {i+1}: ")
    if i == 1:
        danh_sach.insert(1,name)
    else:
        danh_sach.append(name)
        print(danh_sach)
