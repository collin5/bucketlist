#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: settings.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017


SECRET_KEY = "\x84\xaeI\x13\n\x9fa  \n\xdf\x08\xdb'p\x024\x1a\x9d\xc7\x01N\x02\xb9"

# change to other database when in production 
SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format("../sqlite3.db")

# change to false when in production
DEBUG = True
