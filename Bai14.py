print("===Xet Dau Chuyen")

Toan = float(input("Nhap diem Toan: "))
Van = float(input("Nhap diem Van: "))
Anh = float(input("Nhap diem Anh: "))

dtb = (Toan + Van + Anh) / 3
print(f"Diem trung binh: {dtb:.2f}")

if dtb >= 8.5 and Toan >= 9 and Toan > Van and Toan >Anh:
    print("Dau chuyen Toan")
elif dtb >= 8.5 and Van >= 9 and Van >= Anh:
    print("Dau chuyen Van")
elif dtb >= 8.5 and Anh >= 8:
    print("Dau chuyen Anh")
elif dtb >= 8.5:
    print("Dau chuyen Tin")
else:
    print("Khong dau chuyen")

