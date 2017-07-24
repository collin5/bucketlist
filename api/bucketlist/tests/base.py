#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/base.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 24.07.2017
# Last Modified: 24.07.2017

from unittest import TestCase
from api.app import app, db
from abc import ABCMeta
import json


class BaseTestCase(TestCase):
    __metaclass__ = ABCMeta

    @classmethod
    def setUp(ctx):
        ctx.app = app.test_client()
        db.create_all()
        # first create user object
        form = {
            "username": "collins",
            "email": "collins@google.com",
            "password": "validpassword"
        }
        ctx.app.post('/auth/register', data=form)
        # now login to get the user token
        ctx.token = json.loads(ctx.app.post('/auth/login', data={
            "username": "collins",
            "password": "validpassword"
        }).data.decode('utf-8'))['token']

    def test_content_type(self):
        response = self.app.post('/auth/login', data=None)
        self.assertEqual(response.content_type, 'application/json')

    def tearDown(self):
        db.drop_all()
