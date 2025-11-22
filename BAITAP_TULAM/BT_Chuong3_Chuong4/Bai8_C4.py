s = input("Nhập chuỗi: ")

co_hoa = any(ch.isupper() for ch in s)
co_thuong = any(ch.islower() for ch in s)
co_so = any(ch.isdigit() for ch in s)
co_dac_biet = any(not ch.isalnum() for ch in s) #ki tu khong phai so va chu
du_dai = len(s) >= 6

if co_hoa and co_thuong and co_so and co_dac_biet and du_dai:
    print("Mat khau manh.")
else:
    print("Mat khau khong manh")