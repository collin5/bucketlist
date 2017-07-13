#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/auth/tests/test_login.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from unittest import TestCase
from api.app import app
from api.app import db


class LoginTestCase(TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        # create user we are going to use for tests
        form = {"username": "bucketuser",
                "email": "bucket@user.com",
                "password": "password123456"
                }
        self.app.post('/auth/login', data=form)

    def test_login_with_username_successfully(self):
        form = {"username": "bucketuser",
                "password": "password123456"
                }
        response = self.app.post('/auth/login', data=form)
        self.assertEqual(response.status_code, 200)

    def test_login_with_email_successfully(self):
        form = {"email": "bucket@user.com",
                "password": "password123456"
                }

        response = self.app.post('/auth/login', data=form)
        self.assertEqual(response.status_code, 200)

    def test_login_with_wrong_credentials(self):
        form = {"username": "nobody",
                "password": "nobodypassword"
                }
        response = self.app.post('/auth/login/', data=form)
        self.assertEqual(response.status_code, 401)

    def test_login_with_correct_username_wrong_password(self):
        form = {"username": "bucketuser",
                "password": "withwrongpassword"
                }
        response = self.app.post('/auth/login/', data=form)
        self.assertEqual(response.status_code, 401)

    def test_login_with_no_params(self):
        form = {}
        response = self.app.post('/auth/login/', data=form)
        self.assertEqual(response.status_code, 200)

    def test_login_successfully_content(self):
        form = {"username": "bucketuser",
                "password": "password123456"
                }
        response = self.app.post('/auth/login/', data=form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("logged in successfully" in response.content.lower())

    def test_login_with_wrong_credentials_content(self):
        form = {"username": "nobody",
                "password": "loremipsum"
                }
        response = self.app.post('/auth/login', data=form)
        self.assertEqual(response.status_code, 401)
        self.assertTrue("invalid login" in response.content.lower())

        def test_login_with_no_params_content(self):
            form = {}
            response = self.app.post('/auth/login/', data=form)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(
                "please fill all forms" in response.content.lower())

    def tearDown(self):
        db.drop_all()
