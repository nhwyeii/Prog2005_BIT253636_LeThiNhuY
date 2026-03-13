def diem_trung_binh(students):
    tong = sum(students.values())
    so_luong = len(students)
    return tong/so_luong


students = {"hanh":8,"hy":9,"linhden":8.5}
print("Diem trung binh:", diem_trung_binh(students))

