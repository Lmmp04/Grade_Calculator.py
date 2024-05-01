#!/bin/python
#Made by Leo Platti April 2024 - Grade Calculator for practical programming
import math
#Description
quizzes_grades = []
assignments_grades = []
project_grades = []
name = input("Enter students name(as First Last): ")

print("This is a grade calculator created by Leo Platti in April 2024")

#Name & Number of assignments
def get_name_assignments_grades():
    assignments = int(input("Enter the number of Assignments to grade: "))
# Entering Assignment Grades
    for i in range(0, assignments, + 1):
        enter_grade = int(input(f"Enter grade number for an assignment: "))
        assignments_grades.append(enter_grade)
    print(assignments_grades)
    return assignments_grades
get_name_assignments_grades()

#Entering Quizzes
def get_quizzes_grades():
    quizzes = int(input("Enter number of quizzes taken: "))
    #Entering Quiz Grades
    for i in range(0, quizzes, + 1):
        enter_quiz_grade = float(input(f"Enter grade number for quiz: "))
        quizzes_grades.append(enter_quiz_grade)
    return quizzes_grades
get_quizzes_grades()

#Projects
def get_project_grades():
    projects = int(input("Enter number of Projects done: "))
    #Entering Project Grades
    for i in range(0, projects, + 1):
        enter_project_grades = int(input(f"Enter grade number for project: "))
        project_grades.append(enter_project_grades)
    print(project_grades)
    return project_grades
get_project_grades()

#Calculating missed sessions
absences = int(input("How many class sessions did you miss this semester?"))

#Algotrithim and math equations
def algorithim(assignment_grades, quiz_grades, project_grades, name):
    def Assignment_Average(assignment_grades):
        return sum(assignment_grades) / len(assignment_grades)
    def project_average(project_grades):
        return sum(project_grades) / len(project_grades)
    def quiz_average(quiz_grades):
        quizzes_grades.remove(min(quizzes_grades))
        return sum(quiz_grades) / len(quiz_grades)
    #quiz average drops lowest quiz grade built in
    quiz_ave = quiz_average(quiz_grades)
    print(quiz_ave)
    project_ave = project_average(project_grades)
    assignment_ave = Assignment_Average(assignment_grades)
    final_grade = (quiz_ave + project_ave + assignment_ave) /3
#Provide Letter Grade
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
    if final_grade < 65:
        letter_grade = "F"
#Print the report for the user to view
    def display(name, quiz_average, project_average, assignment_average, final_grade, letter_grade):
        print("Name: " + name)
        print("Quiz Averages: ", quiz_ave)
        print("Project Averages: ", project_ave)
        print("Assignment Averages: ", assignment_ave)
        print("Total Average: ", final_grade)
        print("Letter Grade: ", letter_grade)
algorithim(assignments_grades, quizzes_grades, project_grades, name)
