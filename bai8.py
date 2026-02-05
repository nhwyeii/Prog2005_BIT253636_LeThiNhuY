n = int(input())
dao_nguoc = 0
while n > 0:
    dao = dao_nguoc * 10 + n % 10
    n //= 10
print("Số đảo ngược:", dao_nguoc)
