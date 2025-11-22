s= input("Nhập chuỗi: ")

hoa = thuong = so = 0

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    elif ch.isdigit():
        so += 1

print("Ký tự in hoa: ", hoa)
print("Ky tu in thuong: ", thuong)
print("Ký tu so: ", so)