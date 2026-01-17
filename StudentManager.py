from Student import Student
import os

class StudentManger:
    def __init__(self, filename = "student.txt"):
        self.filename = filename
        
        
    def enroll_student(self, student:Student):
        
        with open(self.filename, "a") as file:
            crouse_list = ",".join(student.crouses)
            record = f"{student.get_roll()} - {student.get_name()} - {crouse_list}\n"
            file.write(record)
        print(f"Student {student.get_name()} enrolled Succely")
        
    
    def show_all_students(self):
        print(f"Looking for file at: {os.path.abspath(self.filename)}")
        print("-"*4 + "List of All Enrolled Students" + "-"*4)
        
        if not os.path.exists(self.filename):
            print("No Data Found")
            return
        
        try:
            with open(self.filename, "r") as file:
                for student in file:
                    p = student.strip().split(" - ")
                    
                    if len(p) == 3:
                        roll, name, crouses = p
                        print(f"Roll: {roll}, Name: {name}, Crouses: {crouses}")
        except FileNotFoundError as e:
            print(f"Unknown Error occured: {e}")