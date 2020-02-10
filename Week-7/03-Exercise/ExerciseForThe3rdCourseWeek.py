import random
import os
import csv

class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        grade_list = self.data_sheet.get_grades_as_list()
        return  sum(grade_list) / len(grade_list)

    def list_student(self):
        return [self.name,self.gender,self.data_sheet.list_dataSheet(),self.image_url]

    def get_name(self):
        return self.name

    def get_image_url(self):
        return self.image_url

    def __str__(self):
        return ''.join(self.name + " " + self.image_url + " " + str(self.get_avg_grade()))

class DataSheet():
    def __init__(self,courses=[]):
        self.courses = courses

    def get_grades_as_list(self):
        grade_list = []
        for course in self.courses:
            grade_list.append(int(course.get_grade()))
        return grade_list

    def list_dataSheet(self):
        return [course.list_course() for course in self.courses]

class Course():
    def __init__(self,name,classroom,teacher,ETCS,optional_grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS 
        self.optional_grade = optional_grade

    def get_grade(self):
        return self.optional_grade    

    def list_course(self):
        return [self.name, self.classroom, self.teacher, self.ETCS, self.optional_grade]

def random_corses_and_grades():
    student_corse_list = []
    possible_grades = [-3,0,2,4,7,10,12]
    cource_list = [Course('Mathematics',206,'Ole Larsen',15,random.choice(possible_grades)),Course('Arts',214,'Lone Olsen',5,random.choice(possible_grades)),Course('Society',199,'Anders Andersen',5,random.choice(possible_grades)),Course('Java programming',202,'Allan Alleberg',30,random.choice(possible_grades))]
    for num in range(random.randint(1,len(cource_list))):
        student_corse_list.append(cource_list[num])
    return DataSheet(student_corse_list)

def generate_students(n):
    student_list = []
    first_names=('John','Andy','Joe')
    last_names=('Johnson','Smith','Williams')
    person_gender=('male','female')
    image_urls=('https://pbs.twimg.com/profile_images/1065162126354980864/0rGt5-H7_400x400.jpg','https://pics.me.me/peppe-2735325.png','https://pbs.twimg.com/profile_images/1159563725709488130/slNeABwr.jpg','https://2static1.fjcdn.com/comments/You+filthy+gajin+the+only+peppe+ill+ever+need+is+_5f329c96ef781f28161eed18ace0c6a4.png')

    for number in range(n):
        name = random.choice(first_names)+" "+random.choice(last_names)
        gender = random.choice(person_gender)

        datasheet = random_corses_and_grades()

        immage_url = random.choice(image_urls)

        student_list.append(Student(name,gender,datasheet,immage_url))
    
    to_file = 'C:/Users/rasmu/Desktop/Python/Week-7/03-Exercise/studentFile.csv'

    with open(to_file,'w', newline='') as file_object:
        obj=csv.writer(file_object)
        for person in student_list:
            obj.writerow(person.list_student())

def Read_student_data():
    from_file = 'C:/Users/rasmu/Desktop/Python/Week-7/03-Exercise/studentFile.csv'
    student_obj = []
    with open(from_file) as file_object:
        lines = file_object.readlines()

        for student in lines:
            line = student.split(',')
            name = line[0]
            gender = line[1]
            img = line[len(line)-1]
            data = []
            for num in range(2,len(line)-2,5):
                data.append(Course(line[num].translate(str.maketrans('','','\" \"[]\"')),line[num+1].translate(str.maketrans('','','\" \"[]\"')),line[num+2].translate(str.maketrans('','','\" \"[]\"')),line[num+3].translate(str.maketrans('','','\" \"[]\"')),line[num+4].translate(str.maketrans('','','\" \"[]\"'))))
            dataSheet = DataSheet(data)
            student_obj.append(Student(name,gender,dataSheet,img))

        for obj in student_obj:
            print(str(obj))

        return student_obj

generate_students(7)
Read_student_data()