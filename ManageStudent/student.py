import math


class Student:
    def __init__(self, idStu, nameStu, genderStu, ageStu, scoreMath, scorePhy, scoreChe):
        self.idStu = idStu
        self.nameStu = nameStu
        self.genderStu = genderStu
        self.ageStu = ageStu
        self.scoreMath = scoreMath
        self.scorePhy = scorePhy
        self.scoreChe = scoreChe
        self.gpa = math.ceil(scoreMath + scoreChe + scorePhy)/3
