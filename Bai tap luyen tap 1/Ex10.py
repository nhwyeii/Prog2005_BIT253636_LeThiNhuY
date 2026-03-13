#10
def add_product():
    code = input()
    name = input()
    price = float(input())

    with open("products.txt", "a", encoding="utf-8") as f:
        f.write(f"{code};{name};{price}\n")

    print("them san pham")


def show_products():
    print("danh sach san pham")
    try:
        with open("products.txt", "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())
    except:
        print("khong co du lieu")


def sort_products():
    products = []

    try:
        with open("products.txt", "r", encoding="utf-8") as f:
            for line in f:
                code, name, price = line.strip().split(";")
                products.append((code, name, float(price)))
    except:
        print("khong co du lieu")
        return

    products.sort(key=lambda x: x[2], reverse=True)

    print("danh sach san pham sau giam dan:")
    for p in products:
        print(f"{p[0]};{p[1]};{p[2]}")


while True:
    print("\n===== MENU =====")
    print("1. Thêm sản phẩm")
    print("2. Hiển thị danh sách sản phẩm")
    print("3. Sắp xếp theo giá giảm dần")
    print("4. Thoát")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        show_products()
    elif choice == "3":
        sort_products()
    elif choice == "4":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ")