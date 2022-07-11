#CLASSES,OBJECTS,ATTRIBUTES,METHODS


class Student:
    #constructor when we wont to make of a method
    def __init__(self,first_name,last_name,age,instructor,course):#function inside a class is a method
        #self to refer to the characteristics
        #ATTRIBUTES
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.instructor=instructor
        self.course=course
        #METHOD
    def print_info(self,message):#does not have to have a parameter or arguement unless you want to add on to that specific class
        print(message)
        print(f"name:{self.first_name}{self.last_name}")
        print(f"age:{self.age}")

class Course:
    def __init__(self, data): 
        self.name= data["name"]
        self.instructors= data["instructors"]
        self.program=data["program"]
    def print_instructor_list(self):
        for instrutor in self.instructors:
            print(instrutor)
    def update_instructor(self, new_name, index):
        if index < len(self.instructors):
            self.instructors[index]=new_name
    def print_info(self):
        print(f"Program{self.program}")
        print(f"Name{self.name}")
        self.print_instructor_list()

python={"name":"python/Flask",
        "instructor":["mike","bree","john","ralf"],
        "program":"Full stack"
}
course_python = Course(python)
course_python.update_instructor("ryan mendez",2)

student_alex=Student("alex","johm","40","mike","fundamentals")
student_martha=Student("martha","ann","30","ike","mentals")#have to call on class to use parameters and then set own arguements in the places
print(student_alex.age,student_alex.first_name,student_alex.last_name,student_alex.instructor,student_alex.course)
#this is to target the class and what it holds attributes to give them and use them with arguements
#if it was a function instead of class it would be
# student_alex=__init__()
student_alex.print_info("eeeeeee")#callingfunction while using class parameters and the instances arguements a duo without the other wouldnt work
student_martha.print_info("ooooooo")#you can make other instances and use the class give arguements to the parameters and also add on to current or future functions for more instances not related to the class the function is in
list_students=[]
list_students.append(student_alex)
list_students.append(student_martha)
for student in list_students:
    student.print_info("heythere")
#CHAINING, ASSOCIATING CLASSES ,CLASS ATTRIBUTES CLASS STATIC METHODS
