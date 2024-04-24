from AdressEntity import AdressEntity


class FederalEmployee(AdressEntity):
    def __init__(self, name, function, street, number, zipCode):
        super().__init__(street, number, zipCode)
        self.name = name
        self.function = function

    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName

    def getFunction(self):
        return self.function
    
    def setFunction(self, newFunction):
        self.function = newFunction

    def __str__(self):
        return f"Name: {self.name}\nFunction: {self.function}"


# federalEmployee = FederalEmployee("Klayvert", "Técnico em enfermagem", "rua a", "a", "555555-55")
# print(federalEmployee)