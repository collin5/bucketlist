#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: manage.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from flask_script import Manager
from api.app import app
from api.app import db


manager = Manager(app)

def confirm_action(func):
    def wrap(*args, **kwargs):
        stdin = input("Are you sure you want to {} [Y/N] ".format(func.__doc__))
        if stdin.lower() == 'y':
            return func(*args, **kwargs)
        else:
            return False

    wrap.__name__ = func.__name__
    wrap.__doc__ = func.__doc__
    return wrap

@manager.command
@confirm_action
def migrate():
    """run migrations"""
    db.create_all()

@manager.command
@confirm_action
def drop():
    """drop database"""
    db.drop_all()


if __name__ == "__main__":
    manager.run()
