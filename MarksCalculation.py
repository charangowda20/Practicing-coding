Program: Student Marks and Percentage Calculation
# Program to calculate total marks, percentage, and grade of a student

# Student details
student_name = "Rahul"
roll_number = 101
student_class = "First Year BCA"

# Marks in five subjects
english = 78
maths = 85
science = 90
computer = 88
social_science = 76

# Total marks
total_marks = english + maths + science + computer + social_science

# Maximum marks
maximum_marks = 500

# Percentage calculation
percentage = (total_marks / maximum_marks) * 100

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Display student details
print("----- Student Mark Sheet -----")
print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Class:", student_class)

print("\n----- Subject Marks -----")
print("English:", english)
print("Maths:", maths)
print("Science:", science)
print("Computer:", computer)
print("Social Science:", social_science)

print("\n----- Result -----")
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
