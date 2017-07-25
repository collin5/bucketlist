#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/views.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import app
from flask import request, redirect


@app.route("/")
def index():
    # TODO: will use to launch front end later
    return redirect("{}apidocs".format(request.url), code=302)
