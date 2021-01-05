from canvasapi import Canvas
from keys import C_URL, C_KEY

# SETUP VARIABLES #

canvas = Canvas(C_URL, C_KEY)
account = canvas.get_account(1)
dev_account = canvas.get_account(158)
training_course = canvas.get_course('GROW-W-CNVS', use_sis_id=True)

# FUNCTIONS #


def get_c_user(username):
    uname = username.split('@')[0] + '@wou.edu'
    c_user = canvas.get_user(uname, 'sis_login_id')
    return c_user


def get_c_course(sis_id):
    canvas_course = canvas.get_course(sis_id, use_sis_id=True)
    return canvas_course


def devshell(username, coursename, coursecode):
    canvas_user = get_c_user(username)
    name = coursename + ' DEV'
    code = coursecode + ' DEV'
    new_course = dev_account.create_course(
        course={
            'name': name,
            'course_code': code,
            }
        )
    new_enrollment = new_course.enroll_user(
        canvas_user,
        'TeacherEnrollment',
        enrollment={'role_id': 36},
        )
    return new_course


def sandbox(username):
    canvas_user = get_c_user(username)
    name = canvas_user.name + ' Sandbox'
    new_course = dev_account.create_course(
        course={
            'name': name,
            'course_code': name,
        }
    )
    new_enrollment = new_course.enroll_user(
        canvas_user,
        'TeacherEnrollment',
        enrollment={'role_id': 36},
        )
    return new_course


def training(username):
    canvas_user = get_c_user(username)
    new_enrollment = training_course.enroll_user(
        canvas_user,
        'StudentEnrollment',
        )
    return new_enrollment


def quickstart(username):
    s_box = sandbox(username)
    train = training(username)
    return s_box


def enroll(username, course_id):
    user = get_c_user(username)
    course = get_c_course(course_id)
    new_enrollment = course.enroll_user(
        user,
        'StudentEnrollment',
        )
    return new_enrollment
