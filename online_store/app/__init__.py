#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Simple flask app"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)

app.config["SECRET_KEY"] = "some string"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://online_store"
db = SQLAlchemy(app)

from app import routes
