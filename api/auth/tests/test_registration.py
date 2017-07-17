#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/tests/test_authentication.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from unittest import TestCase
from api.app import app
from api.app import db


class RegisterUserTestCase(TestCase):

    def setUp(self):
        """Create database and tables """
        self.app = app.test_client()
        db.create_all()

    def test_register_user_successfully(self):
        form = {"username": "bucketuser",
                "email": "bucket@user.com",
                "password": "password123456"
                }

        response = self.app.post('/auth/register', data=form)
        self.assertEqual(response.status_code, 200)

    def test_register_user_successfully_content(self):
        form = {"username": "anotheruser",
                "email": "another@email.com",
                "password": "password123456"
                }

        response = self.app.post('/auth/register', data=form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "user anotheruser added successfully" in response.data.decode('utf-8').lower())

    def test_register_user_wrong_email(self):
        form = {"username": "anotheruser",
                "email": "another@",
                "password": "password123456"
                }

        response = self.app.post('/auth/register', data=form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("invalid email" in response.data.decode('utf-8').lower())

    def test_register_user_no_params(self):
        form = {}
        response = self.app.post('/auth/register', data=form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("please fill all fields" in response.data.decode('utf-8').lower())

    def tearDown(self):
        """Remove database"""
        db.drop_all()
