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
                if request.form.get(field, None) is None:
                    return "Please fill all fields"
            return func(*args, **kwargs)
        return wrap
    return decorate
