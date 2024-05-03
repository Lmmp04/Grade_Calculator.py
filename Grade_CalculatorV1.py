#Grade Calculator - Comp Sci - Leo Platti - May 1st 2024
print("Welcome to the CS134 Final Grade Calculator!")
name = input("Enter your name: ")
assignments = int(input("Enter number of Assignments: "))
assignment_weight = input("Enter weight of Assignments (as a decimal): ")
quizzes = int(input("Enter number of Quizzes: "))
quizzes_weight = input("Enter weight of quizzes (as a decimal): ")
projects = int(input("Enter number of Projects: "))
project_weight = input("Enter Weight of Projects (as a decimal): ")
participation_grade = input("Enter Participation Grade: ")
assignment_list = []
project_list = []
quiz_list = []

def get_assign_ave():
    for i in range(0, assignments, + 1):
        enter_assign = int(input("Enter Score for Assignment: "))
        assignment_list.append(enter_assign)
get_assign_ave()
assign_ave = sum(assignment_list) / len(assignment_list)
def get_quiz_ave():
    for i in range(0, quizzes, + 1):
        enter_quiz = int(input("Enter Score for Quiz: "))
        quiz_list.append(enter_quiz)
get_quiz_ave()
quiz_ave = sum(quiz_list) / len(quiz_list)

def get_project_ave(assign_ave, quiz_ave):
    for i in range(0, projects, + 1):
        enter_project = int(input("Enter Score for Project: "))
        project_list.append(enter_project)
    proj_ave = sum(project_list) / len(project_list)
    final_grade = (assign_ave + quiz_ave + proj_ave) / 3
    if final_grade >= 93:
                letter_grade = 'A'
    if  93 <= final_grade <= 100:
                letter_grade = "A"
    if  90 <= final_grade <= 92:
                letter_grade = "A-"
    if 87 <= final_grade <= 89:
                letter_grade = "B+"
    if 83 <= final_grade <= 86:
                letter_grade = "B"
    if 80 <= final_grade <= 82:
                letter_grade = "B-"
    if 77 <= final_grade <= 79:
                letter_grade = "C+"
    if 73 <= final_grade <= 76:
                letter_grade = "C"
    if 70 <= final_grade <= 72:
                letter_grade = "C-"
    if 65 <= final_grade <= 69:
                letter_grade = "D"
    if 65 > final_grade:
                letter_grade = "F"
    print("CS 134 Final Grade for", name, ": ")
    print("Final Grade: ", final_grade, "%")
    print("Letter Grade", letter_grade)
get_project_ave(assign_ave, quiz_ave)
