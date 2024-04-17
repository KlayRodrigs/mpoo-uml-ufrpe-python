
from ClassroomEntity import ClassroomEntity


class CollegeSubjectEntity(ClassroomEntity):
    def __init__(self, name, classroomNumber, limit):
        self.name = name
        self.students = []
        self.teachers = []
        super().__init__(classroomNumber, limit)

    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName
    
    def __str__(self):
        return f"disciplina: {self.name}\nstudents: {self.students}\nteachers: {self.teachers}"

disciplina = CollegeSubjectEntity("Aoba", "2B", 10)
print(disciplina)