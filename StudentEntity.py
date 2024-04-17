from AdressEntity import AdressEntity


class StudentEntity(AdressEntity):
    def __init__(self, name, age, street, number, zipCode):
        super().__init__(street, number, zipCode)
        self.name = name
        self.grades = []
        self.age = age

    def getName(self):
       return self.name
    
    def setName(self, newName):
       self.name = newName

    def getAge(self):
       return self.age
    
    def setAge(self, newAge):
       self.age = newAge

    def getGrades(self):
       return self.grades
    
    def setGrades(self, grade):
       self.grades = grade

    def __str__(self):
       return f"name: {self.name}\nage: {self.age}\ngrades: {self.grades}"


aluno = StudentEntity("Klayvert", "22", "1", "22", "200000")
print(aluno)