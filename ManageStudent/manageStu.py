import math
from student import Student

class manageStudent:
    lst_student = []

    def idStudent(self):
        idStu = 1
        if self.lst_student.__len__() > 0:
            idStu = self.lst_student[0].idStu
            for sv in self.lst_student:
                if idStu < sv.idStu:
                    idStu = sv.idStu
            idStu = idStu + 1
        return idStu
    def addStudent(self):
        idStud = self.idStudent()
        nameStud = input('Name student : ')
        genderStud = input('Gender student : ')
        if int(genderStud) == 0 or genderStud == 'Male' or genderStud == 'male':
            genderStud = 'Male'
        elif int(genderStud) == 1 or genderStud == 'Female' or genderStud == 'female':
            genderStud = 'Female'
        else:
            genderStud = 'Unknown'
        ageStud = int(input('Age student : '))
        scoreMa = float(input('Score Math : '))
        scorePh = float(input('Score Physical : '))
        scoreCh = float(input('Score Chemistry : '))
        sv = Student(idStud, nameStud, genderStud, ageStud, scoreMa, scorePh, scoreCh)
        self.lst_student.append(sv)

    def searchStudent(self, id):
        for sv in self.lst_student:
            if sv.idStu == id:
                return sv
        return False

    def deleteStudent(self, id):
        if self.searchStudent(id) == False:
            print('Không tìm thấy sinh viên có ' + id)
            return False
        else:
            self.lst_student.remove(self.searchStudent(id))
            print('Xóa sinh viên thành công !')
            return True

    def updateStudent(self, id):
        if self.searchStudent(id) == False:
            print('Không tìm thấy sinh viên có ' + id)
        else:
            name = input('Name student : ')
            gender = input('Gender student : ')
            if int(gender) == 0 or gender == 'Male' or gender == 'male':
                gender = 'Male'
            elif int(gender) == 1 or gender == 'Female' or gender == 'female':
                gender = 'Female'
            else:
                gender = 'Unknown'
            age = int(input('Age student : '))
            scoreM = float(input('Score Math : '))
            scoreP = float(input('Score Physical : '))
            scoreC = float(input('Score Chemistry : '))
            sv:Student = self.searchStudent(id)
            #update Student
            sv.nameStu = name
            sv.genderStu = gender
            sv.ageStu = age
            sv.scoreMath = scoreM
            sv.scorePhy = scoreP
            sv.scoreChe = scoreC
            sv.gpa = math.ceil(scoreP+scoreM+scoreC)/3
            print('Cập nhật thành công')

    #Hàm sắp xếp danh sach sinh vien theo tên tăng dần
    def sortByName(self):
        self.lst_student.sort(key=lambda x: x.nameStu, reverse=False)

    def showStudent(self, lst_student):
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "GPA"))
        # hien thi danh sach sinh vien
        if (self.lst_student.__len__() > 0):
            for sv in self.lst_student:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8}"
                      .format(sv.idStu, sv.nameStu, sv.genderStu, sv.ageStu, sv.scoreMath, sv.scorePhy,
                              sv.scoreChe,sv.gpa))
        print("\n")
