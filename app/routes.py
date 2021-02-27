#!/usr/bin/env python3
# -*- coding: utf8 -*-

from app import app
from app.database import create, read, update, delete, scan



@app.route("/users")
def get_all_users():
    return scan()


@app.route("/users/<int:uid>")
def get_one_user(uid):
    return read(uid)


@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.json
    new_id = create(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
    )

    return {"ok": True, "message": "Success", "new_id": new_id}


@app.route("/users/<uid>", methods=["PUT"])
def update_user(uid):
    user_data = request.json
    out = update(int(uid), user_data)
    return {"ok": out, "message": "Updated"}


#NOTHING SEEMS TO WORK THE WAY I WANT IT...STILL HAVING ISSUES TRYING TO FIGURE OUT THIS CODE DOWN BELOW:

# @app.route("/delete/<uid>", methods=["GET"])
# def delete_user():
#     user_data = request.json
#     db = user_db()
#     db.execute('DELETE FROM user WHERE id = ?'[request.form['user_id']])
#     db.commit()

#     return {"ok": out, "message": "Deleted"}
