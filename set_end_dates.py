# Changes end date of all courses and sections for a given Sub-account, Term, and current end date
from canvasapi import Canvas
from keys import C_URL, C_KEY
import sys

# Canvas API setup
canvas = Canvas(C_URL, C_KEY)
account = canvas.get_account(1)
sub_accounts = account.get_subaccounts(recursive=True)
terms = account.get_enrollment_terms()


# Helper function for converting selection to integer or exiting
def isint(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        print('Invalid response')
        sys.exit()


# Finds all courses and sections in a given sub-account and term with a given end date and replaces the end date with
# a new one.
def change_end_date(sub_id, term_id, current_end, new_end):
    sub = canvas.get_account(sub_id)
    courses = sub.get_courses()
    for course in courses:
        sections = course.get_sections()
        if course.enrollment_term_id == term_id:
            if course.end_at == current_end:
                course.update(course={'end_at': new_end})
                print(course.name)
        for section in sections:
            if section.end_at == current_end:
                section.edit(course_section={'end_at': new_end})
                print(section.sis_section_id)


print(C_URL)

# Get term ID
print('')
print('terms:')
term_ids = []
for term in terms:
    term_ids.append(term.id)
    print(term)
current_term_id = isint(input('Enter code for current term: '))
if current_term_id not in term_ids:
    print('Invalid term ID')
    sys.exit()

# Get sub-account ID
print('')
print('subs: ')
sub_ids = []
for sub_account in sub_accounts:
    sub_ids.append(sub_account.id)
    print(sub_account)
sub_account_id = isint(input('Enter sub-account ID: '))
if sub_account_id not in sub_ids:
    print('Invalid sub-account ID')
    sys.exit()

# Get existing end date
print('')
current_end_date = input('Current End Date (e.g. 2021-03-19T07:00:00Z = Mar 19, 2021 at 1am)? ')

# Get new end date
print('')
new_end_date = input('New End Date (e.g. 2021-03-19T07:00:00Z = Mar 19, 2021 at 1am)? ')

change_end_date(sub_account_id, current_term_id, current_end_date, new_end_date)
