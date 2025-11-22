a = input("Nhap chuoi a: ")
b = input("Nhap chuoi b can xoa khoi a: ")

#Tim vi tri xuat hien
vi_tri = a.find(b)

if vi_tri != -1:
    ket_qua = a[:vi_tri] + a[vi_tri + len(b):]
else:
    ket_qua = a #khong tim thay thi giu nguyen

print("Chuoi sau khi xoa: ", ket_qua)
