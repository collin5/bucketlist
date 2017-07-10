#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/views.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import app


@app.route("/auth/login", methods=['POST'])
def login():
    pass


@app.route("/auth/register", methods=['POST'])
def register():
    pass
