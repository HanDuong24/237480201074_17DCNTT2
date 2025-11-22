def tim_nho_nhat(L,a,b):
    doan = L[a:b+1]

    min_doan = doan[0]
    for x in doan[1:]:
        if x < min_doan:
            min_doan = x
    return min_doan

a = int(input("Nhập a= "))
b = int(input("Nhập b= "))
n = int(input("Nhập n= "))

lst = []
for i in range(n):
    while True:
        try:
            x = int(input(f"Nhap so nguyen thu {i} la: "))
            lst.append(x)
            break
        except ValueError:
            print("Vui long nhap lai so nguyen hop le!!")
if 0 < a < b < len(lst):
    KetQua = tim_nho_nhat(lst,a,b)
    print(f"So nho nhat tu vi tri {a} den {b} la: ", KetQua)
else:
    print("Gia tri a, b khong hop le!")


