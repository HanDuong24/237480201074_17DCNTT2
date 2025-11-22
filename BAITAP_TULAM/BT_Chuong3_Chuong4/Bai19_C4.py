def sap_xep_list(lst):
    lst.sort()
    return lst
while True:
    try:
        n = int(input("Nhap n= "))
        if n > 0:
            break
        else:
            print("Moi ban nhap lai so nguyen duong")
    except:
        print("Moi ban nhap lai du liẹu la so!!")

lst = []
for i in range(n):
    while True:
        try:
            x = int(input(f"Phan tu thu {i+1}: "))
            lst.append(x)
            break
        except ValueError:
            print("Moi ban nhap lai so nguyen duong")
KetQua = sap_xep_list(lst)
print(KetQua)