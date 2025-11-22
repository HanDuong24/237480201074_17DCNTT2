'''def ShortString(L):
    if not L:
        return ""
    return min(L, key = len)
print(ShortString(["hello","Welcome to Viet Nam","hi, John"]))
def ShortString(L):
    if not L:
        return ""
    min_str = L[0]
    for i in L[1:]:
        if len(i) < len(min_str):
            min_str = i
    return min_str
print(ShortString(["hello","Welcome to Viet Nam","hi"]))'''
def chuoi_ngan_nhat(lst):
    return min(lst, key=len)
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Nhập n: "))
            break
        except ValueError:
            print("nhập số bất kỳ!")
    lst=[]
    for i in range(n):
        while True:
            try:
                x=input(f"Nhập phần tử thứ {i+1}: ")
                lst.append(x)
                break
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")

print("Chuỗi ngắn nhất là:", chuoi_ngan_nhat(lst))
