from StudentManager import StudentManger
from Student import Student

def main():
    manager = StudentManger()
    
    while True:
        print("* "*6 + "School Management System" + " *"*6)
        print("1. Enroll New Student")
        print("2. Show All Students")
        print("3. Exit")
        
        choice = input("Enter Your Choice: ")
        
        if choice == "1":
            name = input("Enter Your Name: ")
            roll = input("Enter your Roll: ")
            password = input("Enter your Password: ")
            
            student = Student(name, roll, password)
            
            crouse_input = input("Enter Your crouses Name (, sperated): ")
            for crouse in crouse_input.split(","):
                student.enroll_crouse(crouse.strip())
                
            manager.enroll_student(student)
            
            
        elif choice == "2":
            manager.show_all_students()
            
        elif choice == "3":
            print("Exiteing")
            break
        else:           
           print("invaild Input") 
           
           
           
if __name__ == "__main__":
    main()