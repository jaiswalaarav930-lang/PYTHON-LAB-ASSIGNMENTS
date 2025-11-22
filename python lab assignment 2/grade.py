"""
GradeBook Analyzer
Student Name: Aarav Jaiswal
Course: Programming for Problem Solving using Python
University: K.R Mangalam University
Date: 5th October 2025
Instructor: Aryan Sharma
"""

import csv
import statistics

print("=======================================")
print(" Welcome to GradeBook Analyzer CLI Tool ")
print("=======================================")
print("Analyze student marks, assign grades, and view summaries.\n")

# ---------- Functions Section ----------

def calculate_average(marks_dict):
    """Calculate average of all marks"""
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    """Calculate median of marks"""
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    """Find max score and student"""
    max_student = max(marks_dict, key=marks_dict.get)
    return max_student, marks_dict[max_student]

def find_min_score(marks_dict):
    """Find min score and student"""
    min_student = min(marks_dict, key=marks_dict.get)
    return min_student, marks_dict[min_student]

def assign_grades(marks_dict):
    """Assign letter grades"""
    grades = {}
    for student, mark in marks_dict.items():
        if mark >= 90:
            grade = 'A'
        elif mark >= 80:
            grade = 'B'
        elif mark >= 70:
            grade = 'C'
        elif mark >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades[student] = grade
    return grades

def count_grade_distribution(grades_dict):
    """Count students per grade"""
    distribution = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for grade in grades_dict.values():
        distribution[grade] += 1
    return distribution

def display_results(marks, grades):
    """Display formatted table"""
    print("\n================== Grade Report ==================")
    print(f"{'Name':<15}{'Marks':<10}{'Grade':<10}")
    print("-" * 40)
    for student in marks:
        print(f"{student:<15}{marks[student]:<10}{grades[student]:<10}")
    print("-" * 40)
    print()

# ---------- Main Program Section ----------

while True:
    print("Choose an option:")
    print("1. Enter student data manually")
    print("2. Load student data from CSV file (sample provided)")
    print("3. Exit")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        marks = {}
        n = int(input("How many students? "))
        for i in range(n):
            name = input(f"Enter name of student {i+1}: ")
            mark = float(input(f"Enter marks of {name}: "))
            marks[name] = mark

    elif choice == '2':
        # --- CSV Sample Example ---
        # You can create a file "students.csv" in the same folder with this data:
        # Name,Marks
        # Alice,85
        # Bob,92
        # Charlie,67

        filename = input("Enter CSV filename (e.g., students.csv): ")
        marks = {}
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    marks[row['Name']] = float(row['Marks'])
            print("CSV data loaded successfully!")
        except FileNotFoundError:
            print("⚠️ File not found! Please make sure students.csv exists.")
            continue

    elif choice == '3':
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
        continue

    # ---- Analysis ----
    avg = calculate_average(marks)
    median = calculate_median(marks)
    top_student, top_score = find_max_score(marks)
    low_student, low_score = find_min_score(marks)
    grades = assign_grades(marks)
    distribution = count_grade_distribution(grades)

    # ---- Display ----
    display_results(marks, grades)
    print(f"Class Average: {avg:.2f}")
    print(f"Class Median: {median}")
    print(f"Top Student: {top_student} ({top_score})")
    print(f"Lowest Student: {low_student} ({low_score})")

    print("\nGrade Distribution:")
    for grade, count in distribution.items():
        print(f"Grade {grade}: {count} student(s)")

    # ---- Pass/Fail ----
    passed_students = [s for s, m in marks.items() if m >= 40]
    failed_students = [s for s, m in marks.items() if m < 40]

    print(f"\nPassed Students ({len(passed_students)}): {', '.join(passed_students)}")
    print(f"Failed Students ({len(failed_students)}): {', '.join(failed_students)}\n")

    again = input("Do you want to analyze again? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using GradeBook Analyzer!")
        break
