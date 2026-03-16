chuoi = input()

upper = lower = so = ky_tu_dac_biet = khoang_trang = nguyen_am = phu_am = 0

for c in chuoi:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1

    if c.isdigit():
        so += 1
    elif c.isspace():
        ky_tu_dac_biet += 1
    elif not c.isalnum():
        khoang_trang += 1

    if c.lower() in "NhuY":
        nguyen_am += 1
    elif c.isalpha():
        phu_am += 1

print(upper)
print(lower)
print(so)
print(ky_tu_dac_biet)
print(khoang_trang)
print(nguyen_am)
print(phu_am)

