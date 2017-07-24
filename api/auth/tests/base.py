#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/tests/base.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 24.07.2017
# Last Modified: 24.07.2017

from unittest import TestCase
from api.app import app, db
from abc import ABCMeta


class BaseTestCase(TestCase):
    __metaclass__ = ABCMeta

    @classmethod
    def setUp(ctx):
        ctx.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()
