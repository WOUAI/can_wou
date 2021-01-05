from flask import Flask
from flask import request
import ai_functions
import random

# VARIABLES #

app = Flask(__name__)
quote_text = open('quotes', 'r')

# HELPER FUNCTIONS #


def success():
    message = quote_text.readline()[:-2]
    if message == "":
        quote_text.seek(0)
        message = quote_text.readline()[:-2]
    return message

# APP.ROUTE FUNCTIONS #


@app.route('/devshell', methods=['GET'])
def devshell():
    ai_functions.devshell(
        request.args.get('username'),
        request.args.get('coursename'),
        request.args.get('coursecode'),
    )
    return 'Thanks!'


@app.route('/sandbox', methods=['GET'])
def sandbox():
    ai_functions.sandbox(
        request.args.get('username'),
    )
    return success()


@app.route('/training', methods=['GET'])
def training():
    ai_functions.training(
        request.args.get('username'),
    )
    return success()


@app.route('/quick_start', methods=['GET'])
def quickstart():
    ai_functions.training(
        request.args.get('username'),
    )
    ai_functions.sandbox(
        request.args.get('username'),
    )
    return 'Got it, man!'


@app.route('/pratchett', methods=['GET'])
def pratchett():
    return success()


@app.route('/enroll', methods=['GET'])
def enroll():
    ai_functions.enroll(
        request.args.get('username'),
        request.args.get('course_id'),
        )
    return 'There you go, bro.'


@app.route('/kimmy', methods=['GET'])
def kimmy():
    return random.choice(list(open('kimmy_quotes.txt')))

