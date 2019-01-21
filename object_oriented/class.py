class Student:

    #class attribute
    species = "human"

    # instance attribute
    def __init__(self, name, age, idno):
        self.name = name
        self.age = age
        self.idno = idno

    def getname(self):
        return "his name is {}".format(self.name)

    def setname(self, name):
        self.name = name

# instantiate the student class

s = Student("Surya", 26, 2)
t = Student("Tejesh", 26, 3)

# access the class attributes

print("Surya is a {}". format(s.__class__.species))
print("Tejesh is a {}". format(t.__class__.species))

# access to instance attributes

print("{} is {} old and his id is {}". format(s.name, s.age, s.idno))
print("{} is {} old and his id is {}". format(t.name, t.age, t.idno))

# getter and setter
t.setname("Tej")
print(t.getname())
