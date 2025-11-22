s = input("Nhap chuỗi: ")

tong = 0
for ch in s:
    if ch.isdigit():
        tong += int(ch)
print("Tong cac chu so trong chuoi la: ", tong)