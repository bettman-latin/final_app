class Student(object):
    # every object class must have __init__
    def __init__(self, n, e, g, s):
        # instance variables
        self.name = n 
        self.email = e
        self.grade = g
        self.schedule = s

    def __str__(self):
        return "Name: " + self.name + ", Email: " + self.email + " is in grade " + str(self.grade)
# ^^ Default string, what gets printed when object is printed

# vv Functions or methods of Student
    def advance_grade(self):
        if self.grade < 12:
            self.grade += 1

    def print_schedule(self):
        for key, value in self.schedule.items():
            print("{0} Block: {1}".format(key, value))

    def get_B_block(self):
        return self.schedule["B"]


# Creates the student
student1 = Student("Alice Apple", "aapple@lsoc.org", 12, {"B":"Maths", "C":"Earth History", "D":"English", "E":"Chemistry", "G":"Biology"})
print(student1) # Prints the student
print()

student2 = Student("Bob Banana", "bbanana@lsoc.org", 10, {"A":"CS", "B":"Statistics", "D":"Improv", "E":"Racquet Sports", "F":"Creative Writing"})
student2.advance_grade()
print(student2)
student2.print_schedule()

#make a new student
student3 = Student("Carly Carrot", "cc@lsoc", 11, {})













