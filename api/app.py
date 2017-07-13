#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/app.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)
from .auth.models import User
from .bucketlist.models import Bucketlist

# register views
from .views import *
from api.auth.views import *

# run flask app instance
if __name__ == "__main__":
    app.run()
