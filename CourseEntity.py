from CollegeSubjectEntity import CollegeSubjectEntity


class CourseEntity:
    def __init__(self, name):
        self.name = name
        self.universitySubjects = []

    def getName(self):
       return self.name
    
    def setName(self, newName):
       self.name = newName

    def getUniversitySubjects(self):
       return self.universitySubjects
    
    def setUniversitySubjects(self, newUniversitySubjects):
       self.universitySubjects.append(newUniversitySubjects)

    def __str__(self):
       return f"name: {self.name}\nuniversity subjects: {self.universitySubjects}"

curso = CourseEntity("Sistemas de informação")
materia1 = CollegeSubjectEntity("TGA", 15, 30)
curso.setUniversitySubjects(materia1.getName())
print(curso)