#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Routes file: specifies http routes"""

from app import app
from flask import g, request, render_template
import sqlite3


DATABASE = "online_store"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
    
def get_all_users():
    cursor = get_db().execute("select * from user", ())
    results = cursor.fetchall()
    cursor.close()
    return results


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()





#HW1
@app.route('/')
@app.route('/aboutme')
def aboutme():
    user = {
        "first_name": "Miguel",
        "last_name": "RODZ",
        "hobbies": "Mountain bike"
    }
    



# @app.route('/users', methods=["GET", "POST"])
# def get_users():
#     # creating an output dictionary
#     out = {"ok": True, "body": ""}
#     body_list = []
#     if "GET" in request.method:
#         #get_all_users() returns all records from the user table we've created
#         raw_data = get_all_users()
#         for item in raw_data:
#             temp_dict = {
#                 "first_name": item[0],
#                 "last_name": item[1],
#                 "hobbies": item[2]
#             }
#             body_list.append(temp_dict)
#         out["body"] = body_list
#         return out
#     if "POST" in request.method:
#         #create a new user
#         pass






@app.route('/countdown/<int:number>')
def countdown(number):
    return "</br>".join([ str(i) for i in range(number, 0, -1) ])




@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent



@app.route('/users', methods=["GET", "POST"])
def get_users():
    # Creating and output dictionary
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        raw_data = get_all_users()
        for item in raw_data:
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict)
        out["body"] = body_list
        return render_template(
            "base.html",
            first_name=out["body"][0].get("first_name"),
            last_name=out["body"][0].get("last_name"),
            hobbies=out["body"][0].get("hobbies"),
            )
    if "POST" in request.method:
        pass
    if "PUT" in request.method:
        pass
  