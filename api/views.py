#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/views.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import app
from flask import redirect, send_from_directory
import os


@app.route("/")
def index():
    return redirect("/index.html", code=302)


@app.route('/<path:filename>')
def serve_ng(filename):
    """Serve angular files here"""
    root = os.getcwd()
    return send_from_directory(os.path.join(root, 'ngApp', 'dist'), filename)
