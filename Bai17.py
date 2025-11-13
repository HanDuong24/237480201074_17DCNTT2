n = int(input("NHập số nguyên dương n: "))

SumOdd = 0
SumEven = 0

for i in range(1,n):
    if i % 2 == 0:
        SumEven += i
    else:
        SumOdd += i

print(f"Tổng các số lẻ nhỏ hơn {n}: {SumOdd}")
print(f"tổng các số chẵn nhỏ hơn {n}: {SumEven}")