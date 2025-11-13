Tien = int(input("Nhap so tien (VNĐ): "))
ToMenhGia = [50000, 20000, 10000, 5000, 2000, 1000]
print("\n So to tien tuong ung: ")
for MenhGia in ToMenhGia:
    SoTo = Tien // MenhGia
    Tien %= MenhGia
    if SoTo > 0:
        print(f"{MenhGia:>6} VNĐ: {SoTo} to")
if Tien > 0:
    print("Con du", Tien, "dong khong doi duoc!!")