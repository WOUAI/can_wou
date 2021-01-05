# Switches course visibility for all courses in a given subaccount (recursive) for a given term.

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


# Takes sub-account ID, term ID and visibility selection and sets visibility for all selected courses
def set_visibility(sub_id, term_id, vis_bool):
    sub = canvas.get_account(sub_id)
    courses = sub.get_courses()
    for course in courses:
        if course.enrollment_term_id == term_id:
            print(course.name)
            course.update(course={"is_public_to_auth_users": vis_bool})


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

# Get visibility selection
print('')
print('Institution (1)')
print('Course      (2)')
vis_num = isint(input('Set visibility to?: '))
if vis_num == 1:
    visibility_bool = True
elif vis_num == 2:
    visibility_bool = False
else:
    print('Invalid selection')
    sys.exit()

# Set visibility for all selected courses
set_visibility(sub_account_id, current_term_id, visibility_bool)
