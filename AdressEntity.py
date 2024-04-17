class AdressEntity:
    def __init__(self, street, number, zipCode):
      self.street = street
      self.number = number
      self.zipCode = zipCode
    
    def getstreet(self):
       return self.street
    
    def setstreet(self, newStreet):
        self.street = newStreet

    def getnumber(self):
       return self.number
    
    def getzipCode(self):
       return self.zipCode
    
    def __str__(self):
       return f"street: {self.street}\nnumber: {self.number}\nzipcode:{self.zipCode}"
    
endereco = AdressEntity("Rua", 2, "2000000")
print(endereco)