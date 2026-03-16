class SinhVien:
    def __init__(self, ma_sv, ten_sv):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv

    def __eq__(self, other):
        return self.ma_sv == other.ma_sv and self.ten_sv == other.ten_sv

h = SinhVien("BIT253636", "Lê Thị Như Ý")
h1 = SinhVien("BIT252493", "Tào Thị Hải Hạnh")
h2 = SinhVien("BIT253654", "Nguyễn Minh Huyền")
print(h == h1)
print(h == h2)

