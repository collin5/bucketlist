#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/models.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import db
from datetime import datetime


class Bucketlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String)
    todo_on = db.Column(db.DateTime)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow())
