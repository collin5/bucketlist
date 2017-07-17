#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/models.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import db
from datetime import datetime
from random import choice
import string


class User(db.Model):
    __tablename__ = 'tbl_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(64), unique=True)
    salt = db.Column(db.String(64), unique=True)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow())

    @staticmethod
    def make_salt(length=32):
        """Make unique random salt for user or recur"""
        pick_from = 'ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        gen_salt = ""
        for i in range(length):
            gen_salt += choice(pick_from)

        # return if slalt is unique
        if not User.query.filter_by(salt=gen_salt).first():
            return gen_salt
        else:
            return User.make_salt()

    def __repr__(self):
        return self.username
