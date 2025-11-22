import QLSV

def menu():
    print("======CHUONG TRINH QUAN LY SINH VIEN======")
    print("1. Them sinh vien")
    print("2. Xoa sinh vien")
    print("3. Sua sinh vien")
    print("4. Danh sach sinh vien")
    print("5. Thoat")
while True:
    menu()
    chon = input("Moi ban chon chuc nang: ")
    if chon == "1":
        MSSV = input("Nhap MSSV: ")
        HoTen = input("Nhap Ho ten SV: ")
        QLSV.Add_Students(MSSV, HoTen)
        print("Them thanh cong!")
    elif chon == "2":
        MSSV = input("Nhap MSSV can xoa: ")
        if QLSV.Xoa_Students(MSSV):
            print("Da xoa thanh cong")
        else:
            print("Khong tim thay sinh vien can xoa!!")
    elif chon == "3":
        MSSV = input("Nhap MSSV can sua: ")
        tenmoi = input("Nhap ten moi: ")
        if QLSV.CapNhat_Students(MSSV, tenmoi):
            print("Da sua thanh cong")
        else:
            print("Khong tim thay sinh vien can sua!!")
    elif chon == "4":
        ds = QLSV.DS_Students()
        print("====DANH SACH SINH VIEN======")
        if len(ds) == 0:
            print("Danh sach rong")
        else:
            for sv in ds:
                print(f"MSSV: {sv['MSSV']} \nTen: {sv['HoTen']}")
    elif chon == "5":
        print("Thoát chuong trinh!")
        break
    else:
        print("Lua chon khong hop le!!")



