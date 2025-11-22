Students = []
def Add_Students(MSSV, HoTen):
    Students.append({"MSSV":MSSV, "HoTen":HoTen})

def Xoa_Students(MSSV):
    for sv in Students:
        if sv["MSSV"] == MSSV:
            Students.remove(sv)
            return True
        return False

def CapNhat_Students(MSSV, tenmoi):
    for sv in Students:
        if sv["MSSV"] == MSSV:
            sv["HoTen"] = tenmoi
            return True
        return False

def DS_Students():
    return Students

