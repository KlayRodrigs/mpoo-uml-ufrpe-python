from TeacherEntity import TeacherEntity


class DirectorEntity(TeacherEntity):
    def __init__(self, registrationNumber, name, street, number, zipCode):
      self.registrationNumber = registrationNumber
      super().__init__(name, street, number, zipCode)
    
    def getRegistrationNumber(self):
        return self.registrationNumber
    
    def setName(self, newRegistrationNumber):
        self.registrationNumber = newRegistrationNumber

    def __str__(self):
        return f"Registration number: {self.registrationNumber}\n"
    
# directorEntity = DirectorEntity("5495487233", "Klayvert", "rua a", "a", "555555-55")
# print(directorEntity)