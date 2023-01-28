# getters and setters in python

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def getName(self):
        return self.name

    @getName.setter
    def setName(self, name):
        self.name = name

    @getName.deleter
    def delName(self):
        del self.name

p1 = Person("John")
print(p1.getName) # John
p1.setName = "Jack"
print(p1.getName) # Jack
del p1.delName
print(p1.getName) # AttributeError: 'Person' object has no attribute 'name'
