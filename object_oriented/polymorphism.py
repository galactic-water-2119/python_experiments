class Student:

    def study(self):
        print("Student want to study")

    def teach(self):
        print("Student don't want to teach")

class Teacher:

    def study(self):
        print("Teacher don't want to study")

    def teach(self):
        print("Teacher don't want to teach")

# common interface

def study_test(human):
    human.study()

# instantiate objects

varun = Student()
kaul = Teacher()

#passing the object

study_test(varun)
study_test(kaul)