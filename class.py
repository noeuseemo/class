class Student: 
    def __init__(self, id, name, age, group): 
        self.id = id 
        self.name = name 
        self.age = age 
        self.group = group 
 
students = [] 
with open('studentss.txt',encoding = 'utf-8') as file: 
    for line in file: 
        data = line.strip().split(';') 
        
        student = Student(data[0], data[1], data[2], data[3]) 
        students.append(student) 
 
print("|{:<4}|{:<35}|{:<8}|{:<6}|".format("ID", "FIO", "VARIANT", "GROUP")) 
for student in students: 
    print("|{:<4}|{:<35}|{:<8}|{:<6}|".format(student.id, student.name, student.age, student.group))
