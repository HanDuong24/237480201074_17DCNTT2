n = int(input("Nhập số nguyên có 4 chữ số "))
if (1000 <= n <= 9999):
    S = 0
    so = n
    while so > 0:
        S += so % 10
        so //= 10
    print("Tong cac chu so cua", n, "la: ", S)
else:
    print("Vui long nhap so co dung 4 chu so!!")