class Student:
    def __init__(self, name, roll, password):
        self.__name = name
        self.__roll = roll
        self.__password = password
        self.crouses = []
        
        
    def get_name(self):
        return self.__name
    
    def get_roll(self):
        return self.__roll
    
    def enroll_crouse(self, crouse_name):
        self.crouses.append(crouse_name)
        
    def __str__(self):
        if self.crouses:
            crouse_list = ", ".join(self.crouses)
        else:
            crouse_list = "No Crouse"
            
        return f"Roll: {self.__roll} - Name: {self.__name} - Crouses: {crouse_list}"
        
        