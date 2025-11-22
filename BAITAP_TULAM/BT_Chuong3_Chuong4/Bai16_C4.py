def gia_tri_xa_x_nhat(lst,x):
    gia_tri_xa_x_nhat = lst[0]
    do_lech_lon_nhat = abs(lst[0] - x)

    for so in lst[1:]:
        do_lech = abs(so - x)
        if do_lech > do_lech_lon_nhat:
            do_lech_lon_nhat = do_lech
            gia_tri_xa_x_nhat = so
    return gia_tri_xa_x_nhat

while True:
    try:
        x = int(input("Nhap so nguyen x= "))
        break
    except ValueError:
        print("Moi ban nhap lai so nguyen hople!!")
while True:
    try:
        n = int(input("Nhap n= "))
        if n > 0:
            break
        else:
            print("Moi ban nhap lai so nguyen duong")
    except ValueError:
        print("Moi ban nhap lai so !!")

lst = []
for i in range(n):
     while True:
          try:
               x = int(input(f"Phan tu thu {i+1}: "))
               lst.append(x)
               break
          except ValueError:
               print("Moi ban nhap lai so hop le!!")

KetQua = gia_tri_xa_x_nhat(lst,x)
print("Gia tri xa x nhat la: ", KetQua)