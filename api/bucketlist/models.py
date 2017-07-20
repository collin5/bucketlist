#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/models.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import db
from datetime import datetime
from api.auth.models import User


class Bucketlist(db.Model):
    __tablename__ = "tbl_bucketlists"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return self.title

class BucketItem(db.Model):
    __tablename__ = "tbl_bucketitems"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    notes = db.Column(db.String)
    deadline = db.Column(db.DateTime())
    bucketlist_id = db.Column(db.Integer, db.ForeignKey(Bucketlist.id))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow())
