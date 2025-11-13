n = int(input("Nhập số nguyên dương n: "))
Count = 0
Tam = n
while Tam > 0:
    Tam //= 10
    Count +=1

print(f"số {n} có {Count} chữ số.")
