id_to_name = dict()
id_to_class = dict()
id_to_grades = dict()

def add_student(s_id):
    id_to_name[s_id] = input("Enter name: ")
    id_to_class[s_id] = input("Enter class: ")
    print("Enter grades: ")
    grades = []
    for i in range(3):
        grade = int(input("Enter Grade : "))
        grades.append(grade)
    id_to_grades[s_id] = grades    
    print("Student added")

def update_grades(s_id):
    print("Enter new grades: ")
    grades = []
    for i in range(3):
        grade = input("Enter Grade : ")
        grades.append(grade)
    id_to_grades[s_id] = grades
    print("Grades updated")

def calculate_average(s_id):
    total = 0
    for grade in id_to_grades[s_id]:
        total += int(grade)
    return total / 3

def generate_top_student_report():
    classes = dict()
    for s_id, s_class in id_to_class.items():
        if s_class not in classes:
            classes[s_class] = []
        classes[s_class].append(s_id)
    for c, students in classes.items():
        top_student = 0
        top_grade = 0
        for s_id in students:
            grade = 0
            for g in id_to_grades[s_id]:
                grade += int(g)
            if(top_grade < grade):
                top_grade = grade
                top_student = s_id
        print("Top student in class ", c ," is : ", id_to_name[top_student])
