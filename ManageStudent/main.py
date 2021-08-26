from manageStu import manageStudent
import math
# khởi tạo một đối tượng manageStudent để quản lý sinh viên
manager = manageStudent()
while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU**************************")
    print("**  1. Them sinh vien.                               **")
    print("**  2. Cap nhat thong tin sinh vien boi ID.          **")
    print("**  3. Xoa sinh vien boi ID.                         **")
    print("**  4. Hiển thị danh sách sinh viên.                 **")
    print("**  0. Thoát chương trình                            **")
    print("*******************************************************")

    select = input("Nhap tuy chon: ")

    if str(select).isdigit():
        select = int(select)
        if (select == 1):
            print("\n1. Them sinh vien.")
            manager.addStudent()
            print("\nThem sinh vien thanh cong!")
        elif (select == 2):
            if (manager.lst_student.__len__() > 0):
                print("\n2. Cap nhat thong tin sinh vien. ")
                id = int(input('Nhập id của sinh viên cần update : '))
                manager.updateStudent(id)
            else:
                print("\nSanh sach sinh vien trong!")
        elif (select == 3):
            if (manager.lst_student.__len__() > 0):
                print("... Xóa sinh viên ...")
                id = int(input('Nhập id của sinh viên : '))
                if (manager.deleteStudent(id)):
                    print("\nSinh vien co id = ", id, " da bi xoa.")
                else:
                    print("\nSinh vien co id = ", id, " khong ton tai.")
            else:
                print("\nSanh sach sinh vien trong!")
        elif (select == 4):
            if (manager.lst_student.__len__() > 0):
                print("\n7. Hien thi danh sach sinh vien.")
                manager.showStudent(manager.lst_student)
            else:
                print("\nDanh sách sinh viên trống!")
        elif (select == 0):
            print("\nThoát chương trình!")
            break
    else:
        print("\nChức năng này không hợp lệ !")
        print("Vui lòng chọn chức năng !")

