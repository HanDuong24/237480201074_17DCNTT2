n = int(input("nhập vào số nguyên dương n: "))

if n < 2:
    print(f"{n} không phải là số nguyên tố.")
else:
    Count = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            Count += 1
            break
    if Count == 0:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải laf số nguyên tố.")