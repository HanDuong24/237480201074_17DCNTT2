def tim_so_nguyen_duong_nn(lst):
    for x in lst:
        if x > 0:
            return x
        return -1


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
KetQua = tim_so_nguyen_duong_nn(lst)
print("So nguyen duong dau tien la: ", KetQua)