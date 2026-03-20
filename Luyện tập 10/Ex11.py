while True:
    print("1.Bài 1")
    print("2.Bài 2")
    print("3.Thoát")

    chon = int(input())
    if chon == 1:
        path = input("Nhập đường dẫn: ")
        print("Tên file:", lay_ten_file(path))
    elif chon == "2":
        chuoi = input("Nhập chuỗi: ")
        kt = input("Nhập ký tự: ")
        print("Số lần:", chuoi.count(kt))
    elif chon == "3":
        break
    else:
        print("Chọn sai!")