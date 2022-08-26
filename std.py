class Student:
    def details(self):
        return f"name is {self.name}. registration is {self.registration}. age is {self.age}. department is {self.department}. and phone_number is {self.phone_number}"

    def student(self):
        self.name="Praveen"
        self.registration=12011635
        self.age=20
        self.department="CSE" 
        self.phone_number=7979945880
        details=self.student()
    
        print(details())
    # self=student()
    
    # self.name="Praveen"
    # self.registration=12011635
    # self.age=20
    # self.department="CSE"
    # self.phone_number=7979945880
    
    # print(self.details())