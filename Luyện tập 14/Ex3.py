arr = list(map(int, input("Nhập mảng: ").split()))
odd = []
for x in arr:
    if x % 2 != 0:
        odd.append(x)

print("Số lẻ:", odd)
print("Số lượng:", len(odd))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime = []
for x in arr:
    if is_prime(x):
        prime.append(x)

print("Số nguyên tố:", prime)