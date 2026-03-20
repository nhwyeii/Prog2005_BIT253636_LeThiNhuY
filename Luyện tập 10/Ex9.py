class people:
    def __init__(self, ten, tuoi):
        if tuoi < 0:
            raise ValueError("không hợp lệ")
        self._ten = ten
        self._tuoi = tuoi

    def get_ten(self):
        return self._ten

    def set_tuoi(self, tuoi):
        if tuoi < 0:
            raise ValueError("Tuổi phải >= 0")
        self._tuoi = tuoi

    def __str__(self):
        return f"Tên: {self._ten}, Tuổi: {self._tuoi}"

    def xin_chao(self):
        return f"Xin chào, tôi là {self._ten}"

    @classmethod
    def tao_mac_dinh(cls):
        return cls("Hy", 18)

    @staticmethod
    def la_nguoi_lon(tuoi):
        return tuoi >= 18

    def __eq__(self, other):
        return self._ten == other._ten and self._tuoi == other._tuoi


class SinhVien(people):
    def __init__(self, ten, tuoi, mssv):
        super().__init__(ten, tuoi)
        if not mssv:
            raise ValueError("MSSV không hợp lệ")
        self._mssv = mssv

    def __str__(self):
        return f"{super().__str__()}, MSSV: {self._mssv}"


sv = SinhVien("Hạnh", 20, "BIT253636")
print(sv)
print(sv.xin_chao())

nguoi2 = people.tao_mac_dinh()
print(nguoi2)

print(people.la_nguoi_lon(20))