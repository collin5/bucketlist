#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/security/decorators.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 13.07.2017
# Last Modified: 13.07.2017

from flask import request
from functools import wraps
import re


def require_fields(*fields, **kwfields):
    def decorate(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            for field in fields:
                if not request.form.get(field, None):
                    return "Please fill all fields"

            for key, value in kwfields.items():
                if not re.match(r'{}'.format(value), request.form.get(key, None)):
                    return "Invalid {}".format(key)
                
            return func(*args, **kwargs)

        return wrap
    return decorate

def token_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        token = request.form.get('token', None)
        if not token:
            return "Token required for this operation", 403

        return func(*args, **kwargs)
    return wrap
