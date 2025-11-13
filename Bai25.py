try:
    n = int(input("nhập vào số nguyên dương n: "))
    if n <=1:
        print("n phải lớn hơn 1.")
    else:
        S = 0
        k = 0

        while S + (k + 1) < n:
            k += 1
            S += k
        print(f"số k lớn nhất tìm được là: {k}")
        print(f"Khi đó tổng S(k) = 1 + {k} = {S}")

except ValueError:
    print("vui lòng nhập 1 số nguyên hợp lệ.")
