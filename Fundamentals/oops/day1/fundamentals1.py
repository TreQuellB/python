class Student:
    #Constructure
    def __init__(self, first_name, last_name, age, instructor, course):
    #Attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.instructor = instructor
        self.course = course
#Methos
def print_info(self, message):
    print(message)
    print(f"Name:{self.first_name}{self.last_name}")
    print(f"Age:{self.age}")
    print(f"Instructor{self.instructor}")
    print(f"Course{self.course}")
#creating an object/ making a instance of the student class
student_alex = Student("Alex", "Miller", 23, "Nichole", "Fundamentals")
print(student_alex.age)

student_alex.print_info("lex", "Mill", 29, "chole", "Fun")
student_alex.print_info("hey there")
