#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/tests/test_authentication.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from unittest import TestCase
from flask import request, url_for
from api.app import db


class RegisterUserTestCase(TestCase):

    def setUp(self):
        """Create database and tables """
        db.create_all()

    def test_register_user_successfully(self):
        form = {"username": "bucketuser",
                "email": "bucket@user.com",
                "password": "password123456"
                }

        response = request.post(url_for('register'), form)
        self.assertEqual(response.status_code, 200)

    def test_register_user_successfully_content(self):
        form = {"username": "anotheruser",
                "email": "another@email.com",
                "password": "password123456"
                }

        response = request.post(url_for('register'), form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "user registered successfully" in response.content.lower())

    def test_register_user_no_params(self):
        form = {}
        response = request.post(url_for('register'), form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("please fill all fields" in response.content.lower())

    def tearDown(self):
        """Remove database"""
        db.drop_all()
