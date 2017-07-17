#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/security/decorators.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 13.07.2017
# Last Modified: 13.07.2017

from flask import request
import re


def require_fields(*fields, **kfields):
    def decorate(func):
        def wrap(*args, **kwargs):
            for field in fields:
                if not request.form.get(field, None):
                    return "Please fill all fields"

            for key, value in kfields.items():
                if not re.match(r'{}'.format(value), request.form.get(key, None)):
                    return "Invalid {}".format(key)
                
            return func(*args, **kwargs)

        wrap.__name__ = func.__name__
        wrap.__doc__ = func.__name__
        return wrap
    return decorate
