'''def Vitri_MAX(L):
    if not L:
        return -1
    return L.index(max(L))
print(Vitri_MAX([1,4,6,2,7,2,9,7]))'''
'''#en en
def Vitri_MAX(L):
    if not L:
        return -1
    GTLN = L[0]
    Vitri = 0
    for i in range(1,len(L)):
        if L[i] > GTLN:
            GTLN = L[i]
            Vitri = i
    return Vitri
print(Vitri_MAX([4,1,5,7,3,9,0,2]))'''

def vitriMAX(lst):
    max_value = max(lst)
    return lst.index(max_value) + 1
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Nhập n: "))
            break
        except ValueError:
            print("Nhập số bất kỳ!")
    lst = []
    for i in range(n):
        while True:
            try:
                x = int(input(f"Nhap phan tu thu {i+1}: "))
                lst.append(x)
                break
            except ValueError:
                print("Vui long nhap lai so nguyen hợp lệ!!")
print("Danh sach vua nhap: ", lst)
print("Vi tri gia tri lon nhat: ", vitriMAX(lst))