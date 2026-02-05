def giaithua(n):
    if n == 0 or n == 1:
        return 1
    return n * giaithua(n - 1)

n = int(input())
print("Giai thừa =", giaithua(n))
