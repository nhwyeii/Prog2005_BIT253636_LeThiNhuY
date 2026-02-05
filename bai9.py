n = input()
so_lon_nhat = n[0]

for ch in n:
    if ch > so_lon_nhat:
        so_lon_nhat = ch

print("Chữ số lớn nhất:", so_lon_nhat)
