from canvasapi import Canvas
from keys import C_URL, C_KEY
import csv
import sys

canvas = Canvas(C_URL, C_KEY)
account = canvas.get_account(1)

row_list = [["First Name", "Middle Name", "Last Name", "Email", "Student ID"]]
try:
    crn = sys.argv[1]
except:
    crn = input('CRN? ')

course = canvas.get_course(crn, use_sis_id=True)
enrollments = course.get_enrollments()
for enrollment in enrollments:
    if enrollment.role == 'StudentEnrollment':
        student = canvas.get_user(enrollment.user_id)
        name = student.name.split(" ", 1)
        student_row = [name[0], "", name[1], student.email, student.sis_user_id]
        row_list.append(student_row)
for row in row_list:
    print(row)

filename = str(crn) + '.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
