
class Person:
    def __init__(self,name , age ):
        self.name = name
        self.age = age
        pass
        
    def introduction(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

        
class Student(Person):
    def __init__(self, name, age , student_id):
        self.student_id = student_id
        super().__init__(name, age ,)
    def introduction(self):
        return f"{self.name} ,(ID:{self.student_id}, age {self.age})".strip().lower()
    pass




class Teacher(Person):
    def __init__(self, name, age , subject):
        super().__init__(name, age)
        self.subject = subject
    def introduction(self):
    
        return f'{self.name} ,{self.subject} , age {self.age})'



student1 = Student("Yehia" , 18, '20223')
teacher1 = Teacher("Michael" ,39 , 'mathematics')
student1.introduction()
print(teacher1.introduction())
print(student1.introduction())