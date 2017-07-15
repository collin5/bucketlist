#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/security/decorators.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 13.07.2017
# Last Modified: 13.07.2017

from flask import request


def require_fields(*fields):
    def decorate(func):
        def wrap(*args, **kwargs):
            for field in fields:
                if not request.form.get(field, None):
                    return "Please fill all fields"
            return func(*args, **kwargs)

        wrap.__name__ = func.__name__
        wrap.__doc__ = func.__name__
        return wrap
    return decorate
