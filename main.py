import json
from abc import ABC,abstractmethod
from pathlib import Path

database = "school_data.json"
data = {"students" : [],"teachers" :[]}

if Path(database).exists():
    with open(database,'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():
    with open(database,"w") as f:
        json.dump(data,f,indent=4)

class persons(ABC):

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass 

    @abstractmethod
    def show_details(self):
        pass
   
    @staticmethod
    def validate_email (email):
        if "@" in email and "." in email:
            return True
        else:
            return False
        
    

class student(persons):
     
    def get_roles(self):
        return "student"
    
    def register(self):
        name = input("Enter your name :-")
        age = int(input("Enter your age :-"))
        email = input("Enter youe email :-")
        roll_no = input("Enter your roll number :-")
  
        if not persons.validate_email(email):
            print("invalid email:")
            return
        
        for i in data['students']:
            if i ['roll_no'] == roll_no:
                print("student already exits")
                return
        
        data['students'].append({
            "name" : name,
            "age"  : age,
            "email" :email,
            "roll_no" : roll_no,
            "grades": {}
        })

        save()
        print(f"student {name} register")

  
    def show_details(self):
        roll_no = input("roll no :-")
        for s in data['students']:
            if s ['roll_no'] == roll_no:
                grades = s['grades']
                avg = sum(grades.values())/len(grades) if grades else 0

                print (f"\n name : {s['name']}")
                print (f" roll no: {s['roll_no']}")
                print (f" grades: {grades}")
                print (f" average : {avg:.1f}")
                return

    

    def add_grade(self):
        roll_no = input("tell the roll number :-")
        subject = input("subject :")
        marks = float(input ("marks :"))


        for i in data['students']:
            if i ["roll_no"] == roll_no:
                i ['grades'][subject] = marks
                save()
                print("grade added successfully")
            return
        print("student not found")

class teacher(persons):
     def get_roles(self):
        return "teachers"
     
     def register(self):
        name = input("Enter your name :-")
        age = int(input("Enter your age :-"))
        email = input("Enter youe email :-")
        subject = input("enter your subject :-")
        emp_id = input("Enter your emp_id number :-")
    
        if not persons.validate_email(email):
            print("invalid email:")
            return
        
        for i in data['teachers']:
            if i ['emp_id'] == emp_id:
                print("student already exits")
                return
        

        data['teachers'].append({
            "name" : name,
            "age"  : age,
            "email" :email,
            "subject":subject,
            "emp_id" : emp_id,
        })
        save()
        print(f"Teacher {name} registerd")

     def show_details(self):
        emp_id = input("employee_id")
         
        for t in data ['teachers']:
            if t["emp_id"] == emp_id:
                print(f"\n name : {t['name']}")
                print(f" subject : {t['subject']}")
                print(f" emp id : {t['emp_id']}")
                return
        print("teacher not found.")    
    
stud = student()
tech = teacher()

print("press 1 to register a  student ")
print("press 2 to register a  teacher ")
print("press 3 to add grades ")
print("press 4 to show a student details ")
print("press 5 to show a teacher details ")


choice = int(input("please enter your choice :-"))

if choice == 1:
    stud.register()

elif choice == 2:
    tech.register()

elif choice == 3:
    stud.add_grade()

elif choice == 4:
    stud.show_details()

elif choice == 5:
    tech.show_details()

