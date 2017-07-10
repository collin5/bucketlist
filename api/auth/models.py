#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/models.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(64), unique=True)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return self.username
