#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/security/decorators.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 13.07.2017
# Last Modified: 13.07.2017

from flask import request, jsonify
from functools import wraps
from datetime import timedelta
import re


def require_fields(*fields, **kwfields):
    def decorate(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            for field in fields:
                if not request.form.get(field, None):
                    return jsonify({
                        "error_msg": "Please fill all fields"
                    })

            for key, value in kwfields.items():
                if not re.match(r'{}'.format(value), request.form.get(key, None)):
                    return jsonify({
                        "error_msg": "Invalid {}".format(key)
                    })

            return func(*args, **kwargs)

        return wrap
    return decorate


def token_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        token = request.headers.get('token', None)
        if not token:
            return jsonify({
                "error_msg": "Token required for this operation"
            }), 403

        return func(*args, **kwargs)
    return wrap
