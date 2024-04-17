class ClassroomEntity:
    def __init__(self, classroomNumber, limit):
        self.classroomNumber = classroomNumber
        self.limit = limit

    def getClassroomNumber(self):
       return self.classroomNumber
    
    def setClassroomNumber(self, newClassroomNumber):
       self.classroomNumber = newClassroomNumber

    def getLimit(self):
       return self.limit
    
    def setLimit(self, newLmit):
       self.limit = newLmit

    def __str__(self):
       return f"class number: {self.classroomNumber}\nstudents limit: {self.limit}"
    
sala = ClassroomEntity(1, 10)
print(sala)