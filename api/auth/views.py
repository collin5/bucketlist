#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/views.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import app
from api.app import db
from flask import request
from .security.decorators import require_fields 
from .models import User

@app.route("/auth/login/", methods=['POST'])
def login():
    pass


@app.route("/auth/register", methods=['POST'])
@require_fields('username', 'email', 'password')
def register():
    username, email = request.form['username'], request.form['email']
    password = request.form['password']
    if User.query.filter_by(username=username).first():
        return "User {} already exists".format(username)
    else:
        user = User(username=username, email=email, password=password) 
        db.session.add(user)
        return "User added successfully"


