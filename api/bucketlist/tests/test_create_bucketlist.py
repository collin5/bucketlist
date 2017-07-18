#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_create_bucketlist.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 17.07.2017
# Last Modified: 17.07.2017

import unittest
from unittest import TestCase
from api.app import app, db


class CreateBucketList(TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        # first create user object
        form = {
            "username": "collins",
            "email": "collins@google.com",
            "password": "validpassword"
        }
        self.app.post('/auth/register', data=form)
        # now login to get the user token
        self.token = self.app.post('/auth/login', data={
            "username": "collins",
            "password": "validpassword"
        })

    @unittest.skip
    def test_create_bucketlist_successfully(self):
        form = {
            "title": "My list",
            "description": "lorem ipsum blah blah",
            "token": self.app.token
        }
        response = self.app.post('/bucketlist', data=form)
        self.assertEqual(response.status_code, 200)

    @unittest.skip
    def test_create_bucketlist_duplicate(self):
        form = {
            "title": "My list",
            "description": "lorem ipsum blah blah",
            "token": self.token
        }
        response = self.app.post('/bucketlist', data=form)
        self.assertEqual(response.status_code, 200)

        dup_response = self.app.post('/bucketlist', data=form)
        self.assertEqual(dup_response.status_code, 200)
        self.assertTrue("list my list already exists" in dup_response.data.decode('utf-8').lower())



    @unittest.skip
    def test_create_bucketlist_no_token(self):
        form = {
            "title": "My another list",
            "description": "lorem ipsum dor yeah yeah"
        }
        response = self.post('/bucketlist', data=form)
        self.assertEqual(response.status_code, 403)

    @unittest.skip
    def test_create_bucketlist_successfully_message(self):
        form = {
            "title": "My list",
            "description": "lorem ipsum blah blah",
            "token": self.token
        }
        response = self.app.post('/bucketlist', data=form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "list my list was created successfully" in response.data.decode('utf-8').lower())

    @unittest.skip
    def test_create_bucketlist_no_token_message(self):
        form = {
            "title": "My another list",
            "description": "lorem ipsum dor yeah yeah"
        }
        response = self.app.post('/bucketlist', data=form)
        self.assertEqual(response.status_code, 403)
        self.assertTrue("no token" in response.data.decode('utf-8').lower())

    def tearDown(self):
        db.drop_all()
