#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/tests/test_login.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from unitest import TestCase
from flask import request, url_for
from api.app import db


class LoginTestCase(TestCase):

    def setUp(self):
        db.create_all()
        # create user we are going to use for tests
        form = {"username": "bucketuser",
                "email": "bucket@user.com",
                "password": "password123456"
                }
        request.post(url_for("register"), form)

    def test_login_with_username_successfully(self):
        form = {"username": "bucketuser",
                "password": "password123456"
                }
        response = request.post(url_for("login"), form)
        self.assertEqual(response.status_code, 200)

    def test_login_with_email_successfully(self):
        form = {"email": "bucket@user.com",
                "password": "password123456"
                }

        response = request.post(url_for("login"), form)
        self.assertEqual(response.status_code, 200)

    def test_login_with_wrong_credentials(self):
        form = {"username": "nobody",
                "password": "nobodypassword"
                }
        response = request.post(url_for('login'), form)
        self.assertEqual(response.status_code, 403)

    def test_login_with_correct_username_wrong_password(self):
        form = {"username": "bucketuser",
                "password": "withwrongpassword"
                }
        response = request.post(url_for('login'), form)
        self.assertEqual(response.status_code, 403)

    def test_login_with_no_params(self):
        form = {}
        response = request.post(url_for('login'), form)
        self.assertEqual(response.status_code, 200)

    def test_login_successfully_content(self):
        form = {"username": "bucketuser",
                "password": "password123456"
                }
        response = request.post(url_for('login'), form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("logged in successfully" in response.content.lower())

    def test_login_with_wrong_credentials_content(self):
        form = {"username": "nobody",
                "password": "loremipsum"
                }
        response = request.post(url_for('login'), form)
        self.assertEqual(response.status_code, 403)
        self.assertTrue("invalid login" in response.content.lower())

        def test_login_with_no_params_content(self):
            form = {}
            response = request.post(url_for('login'), form)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(
                "please fill all forms" in response.content.lower())

    def tearDown(self):
        db.drop_all()