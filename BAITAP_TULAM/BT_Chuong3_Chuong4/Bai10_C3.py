'''def Even(n):
    return n % 2 == 0

def Perfect_Number(n):
    if n <= 0:
        return False
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

#So nguyen to
def Prime_Number(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def Perfect_Square_Number(n):
    return int(n ** 0.5) ** 2 == n

def ucln(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a,b):
    return a * b // ucln(a, b)

def nguyen_to_cung_nhau(a,b):
    return ucln(a, b) == 1

n = int(input("Nhập n= "))
a = int(input("Nhập a= "))
b = int(input("Nhập b= "))
print(Even(9))
print(Perfect_Number(6))
print(Prime_Number(7))
print(Perfect_Square_Number(9))
print(ucln(5,7))
print(bcnn(23,64))
print(nguyen_to_cung_nhau(9,11))'''
def so_chan(n):
    return n % 2 == 0

def so_hoan_hao(n):
    if n <= 0:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def so_chinh_phuong(n):
    return int(n**0.5)**2 == n

def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return abs(a*b) // ucln(a, b)

def nguyen_to_cung_nhau(a, b):
    return ucln(a, b) == 1

if __name__ == "__main__":
    while True:
        try:
            a = int(input("Nhập a: "))
            break
        except ValueError:
            print("nhập số bất kỳ!")
    while True:
        try:
            b = int(input("Nhập b: "))
            break
        except ValueError:
            print("nhập số bất kỳ!")
    while True:
        try:
            n = int(input("Nhập n: "))
            break
        except ValueError:
            print("nhập số bất kỳ!")

print("Số chẵn: ",so_chan(n))
print("Số hoàn hảo: ",so_hoan_hao(n))
print("Số nguyên tố: ",so_nguyen_to(n))
print("Số chính phương: ",so_chinh_phuong(n))
print("UCLN =", ucln(a, b))
if nguyen_to_cung_nhau(a, b):
    print("a và b nguyên tố cùng nhau")
else:
    print("Không nguyên tố cùng nhau")
print("BCNN =", bcnn(a, b))

