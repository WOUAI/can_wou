# Takes in a CRN and returns a student import file for wise

from canvasapi import Canvas
from keys import C_URL, C_KEY
import csv
import sys

# CanvasAPI setup
canvas = Canvas(C_URL, C_KEY)
account = canvas.get_account(1)

# List of rows that will become the CSV - Includes wise import headers as first row
row_list = [["First Name", "Middle Name", "Last Name", "Email", "Student ID"]]

# Gets CRN from first command line argument - If none, asks for one.
try:
    crn = sys.argv[1]
except:
    crn = input('CRN? ')

# Gets course and course enrollments
course = canvas.get_course(crn, use_sis_id=True)
enrollments = course.get_enrollments()

# Finds all student enrollments in the course and adds them to the row_list table
for enrollment in enrollments:
    if enrollment.role == 'StudentEnrollment':
        student = canvas.get_user(enrollment.user_id)
        name = student.name.split(" ", 1)
        student_row = [name[0], "", name[1], student.email, student.sis_user_id]
        row_list.append(student_row)

# Prints out resulting table to the console
for row in row_list:
    print(row)

# Writes table to CSV file in working directory named after the CRN
filename = str(crn) + '.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
