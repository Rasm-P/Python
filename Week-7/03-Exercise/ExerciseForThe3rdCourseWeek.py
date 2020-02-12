import random
import os
import csv
import matplotlib.pyplot as plt

#Ex 1
class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
        self.avg = self.get_avg_grade()

    def get_avg_grade(self):
        grade_list = self.data_sheet.get_grades_as_list()
        return  sum(grade_list) / len(grade_list)

    def list_student(self):
        return [self.name,self.gender,self.avg,self.data_sheet.list_dataSheet(),self.image_url]

    def get_name(self):
        return self.name

    def get_image_url(self):
        return self.image_url

    def __str__(self):
        return ''.join(self.name + " " + self.image_url + " " + str(self.get_avg_grade()))

    def progression(self):
        total_etcs = 0
        for num in self.data_sheet.courses:
            if not int(num.optional_grade) <= 0:
                total_etcs += int(num.ETCS)
        return total_etcs / 150 * 100

    def list_of_courses(self):
        return self.data_sheet.courses

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
    cource_list = [Course('Mathematics',206,'Ole Larsen',30,random.choice(possible_grades)),Course('Arts',214,'Lone Olsen',30,random.choice(possible_grades)),Course('Society',199,'Anders Andersen',30,random.choice(possible_grades)),Course('Java programming',202,'Allan Alleberg',30,random.choice(possible_grades)),Course('Python programming',188,'Ak Bk',30,random.choice(possible_grades))]
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
            for num in range(3,len(line)-2,5):
                data.append(Course(line[num].translate(str.maketrans('','','\" \"[]\"')),line[num+1].translate(str.maketrans('','','\" \"[]\"')),line[num+2].translate(str.maketrans('','','\" \"[]\"')),line[num+3].translate(str.maketrans('','','\" \"[]\"')),line[num+4].translate(str.maketrans('','','\" \"[]\"'))))
            dataSheet = DataSheet(data)
            student_obj.append(Student(name,gender,dataSheet,img))
    
    sorted_people = sorted(student_obj, key=lambda item: item.avg, reverse=True)
    for obj in sorted_people:
            print(str(obj))

    return sorted_people

def plot_graph(sorted_list):
    x_vals,y_vals = zip(*[(str(i.name),float(i.avg)) for i in sorted_list])

    plt.bar(x_vals, y_vals, width=0.5, align='center')
    title = 'Distribution of names and avg grades'
    plt.title(title, fontsize=12)
    plt.xlabel("Student names", fontsize=10)
    plt.ylabel("Grade avg", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()

def distribution_of_study_progression(sorted_list):
    study_progression = {}
    for stu in sorted_list:
        if stu.progression() not in study_progression:
            study_progression[stu.progression()] = 1
        else:
            study_progression[stu.progression()] = study_progression[stu.progression()] + 1
    plt.bar(study_progression.keys(), study_progression.values()) 
    title = 'Bar chart of distribution of study progression'
    plt.title(title, fontsize=12)
    plt.xlabel("Study progression in %", fontsize=10)
    plt.ylabel("number of students", fontsize=10)
    plt.axis((-5,105,0,len(sorted_list)))
    plt.show()

#Ex 2
def closest_to_completing(sorted_list):
    comp_list = []
    try:
        if len(sorted_list) >= 3:
            comp_list = [sorted_list[0],sorted_list[1],sorted_list[2]]
        else:
            raise NotEnoughStudentsException('Oh no, length is only {}!'.format(len(sorted_list)))
    except NotEnoughStudentsException:
        comp_list = ['The list was shorter than 2!']

    closest_to_completion(comp_list)

class NotEnoughStudentsException(ValueError):
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)
        
def closest_to_completion(students):
    to_file = 'C:/Users/rasmu/Desktop/Python/Week-7/03-Exercise/closest_to_completion.csv'
    with open(to_file,'w', newline='') as file_object:
        obj=csv.writer(file_object)
        if len(students) > 1:
            for person in students:
                obj.writerow(person.list_student())
        else:
            obj.writerow(students)

#3
def student_pie(students):
    study_progression = {}
    for stu in students:
        if stu.progression() not in study_progression:
            study_progression[stu.progression()] = 1
        else:
            study_progression[stu.progression()] = study_progression[stu.progression()] + 1
    
    fig1, ax1 = plt.subplots()
    ax1.pie(study_progression.values(), labels=study_progression.keys(), autopct=lambda p:'{:.2f}%({:.0f})'.format(p,(p/100)*sum(study_progression.values())), shadow=True, startangle=90)
    ax1.set_aspect('equal')
    ax1.legend(study_progression.keys(), loc='upper right')
    plt.show()

def taken_each_course(students):
    male_list = []
    female_list = []
    for student in students:
        if student.gender == 'male':
            male_list.append(student)
        else:
            female_list.append(student)

    female_list = bar_course_number_of_student_list(female_list)
    male_list = bar_course_number_of_student_list(male_list)

    plt.bar(female_list.keys(), female_list.values(), color='red') 
    plt.bar(male_list.keys(), male_list.values(), color='blue') 
    title = 'Bar chart of distribution of number of students for each course (Male and Female)'
    plt.title(title, fontsize=12)
    plt.xlabel("Courses", fontsize=10)
    plt.ylabel("number of students", fontsize=10)
    plt.show()

def bar_course_number_of_student_list(students):
    study_progression = {}
    for stu in students:
        for course in stu.list_of_courses():
            if course.name not in study_progression:
                study_progression[course.name] = 1
            else:
                study_progression[course.name] = study_progression[course.name] + 1 
    return study_progression

#1
generate_students(27)
Read_student_data()
plot_graph(Read_student_data())
distribution_of_study_progression(Read_student_data())

#2
closest_to_completing(Read_student_data())

#3
student_pie(Read_student_data())
taken_each_course(Read_student_data())