def kiem_tra_list_tang_dan(lst):
    while True:
        try:
            n = int(input("Nhap n= "))
            if n > 0:
                break
            else:
                print("Moi ban nhap lai n nguyen duong!!")
        except ValueError:
            print("Moi ban nhap lai du lieu bang so!!")


    for i in range(n):
        while True:
            try:
                x = int(input(f"Nhap phan tu thu {i + 1}: "))
                lst.append(x)
                break
            except ValueError:
                print("Moi ban nhap lai du lieu bang so!!")
    if len(lst) == 0:
        print("\nDanh sach rong")
        return True
    if len(lst) == 1:
        print(f"\nDanh sach da nhap la: {lst}")
        print("Danh sach co 1 phan tu")
        return True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            print(f"\nDanh sach da nhap la: {lst}")
            print(f"\nTai vi tri {i}, gia tri {lst[i]} > {lst[i + 1]} ")
            return False
    print(f"\nDanh sach da nhap la: {lst}")
    print("\nDanh sach da duoc sap xep ")
    return True
lst = []
KetQua = kiem_tra_list_tang_dan(lst)
print(KetQua)