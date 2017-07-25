#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: settings.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017
import os


SECRET_KEY = os.getenv(
    'SECRET_KEY') or "\x84\xaeI\x13\n\x9fa  \n\xdf\x08\xdb'p\x024\x1a\x9d\xc7\x01N\x02\xb9"

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', "postgres:///{}".format("bucketlist"))

# change to false when in production
DEBUG = False if os.environ.get('PRODUCTION', False) else True

SQLALCHEMY_TRACK_MODIFICATIONS = False
