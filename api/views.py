#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/views.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import app


@app.route("/")
def index():
    return "Frontend still under construction :)"
