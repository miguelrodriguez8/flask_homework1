#!/usr/bin/env python3

"""HTTP route definitions"""

from app import app


@app.route("/")
def index():
    return "Hello World!"

#HOMEWORK 1
@app.route("/aboutme")
def about_me():
    my_dictionary = dict()
    my_dictionary["first_name"] = "Miguel"
    my_dictionary["last_name"] = "Rodriguez"
    my_dictionary["hobbies"] = "Mountain biking"
    return my_dictionary