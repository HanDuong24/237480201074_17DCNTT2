def kiem_tra_tich_lan_can(lst):
    if len(lst) < 3:
        print("\nDanh sach qua ngan")
        vitrilancan = -1
    for i in range(1, len(lst) - 1):
        if lst[i] == lst[i - 1] * lst[i + 1]:
            print(f"\nDanh sach thoa dieu kien: {lst[i]} = {lst[i - 1]} * {lst[i + 1]} va co 2 gia tri lan can lan luot la ({lst[i -1]}, {lst[i + 1]}) ")
            vitrilancan = i
    return vitrilancan

lst = []
while True:
    try:
        n = int(input("Nhap n= "))
        if n > 0:
            break
        else:
            print("\nMoi ban nhap lai n nguyen duong")
    except ValueError:
        print("Moi ban nhap lai du lieu so!!")
for i in range(n):
    while True:
        try:
            x = int(input(f"Phan tu thu {i + 1}: "))
            lst.append(x)
            break
        except ValueError:
            print("Moi ban nhap lai du lieu so!!")
KetQua = kiem_tra_tich_lan_can(lst)
print(KetQua)