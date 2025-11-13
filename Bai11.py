n = int(input("Nhap so nguyen duong n: "))

if n % 5 == 0 and n % 7 == 0:
    print(n, "chia het cho ca 5 va 7.")
else:
    print(n, "khong chia het cho ca 5 va 7.")