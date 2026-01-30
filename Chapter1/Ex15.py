for _ in range(int(input())):
    name = str(input())
    diem = list(map(float,input().split()))
    trung_binh = 0
    for i in diem:
        trung_binh += i
    print(f"Ten : {name} Diem trung binh : {trung_binh/len(diem)}")
