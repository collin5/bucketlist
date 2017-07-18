#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_get_bucketlists.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 18.07.2017
# Last Modified: 18.07.2017

from api.app import app
from unittest import TestCase, skip

class GetBucketlistsTestCase(TestCase):

    def setUp(self):
        self.app = app.test_client()
        # first register test user
        reg_form = {
                "username": "collins",
                "email": "collins@andela.com",
                "password": "validpass"
                }
        self.app.post('/auth/register', data=reg_form)
        self.token = self.app.post('/auth/login', data={
            "username": "collins",
            "password": "validpass"
            })
        # Add bucket list
        first_bucket = {
                "title": "First bucket",
                "description": "lorem ipsum blah blah "
                }
        second_bucket = {
                "title": "Second bucket",
                "description": "lorem from second bucket is awesome"
                }
        self.app.post('/auth/bucketlists', first_bucket)
        self.app.post('/auth/bucketlists', second_bucket)
        

    @skip
    def test_get_bucketlist_successfully(self):
        form = {
                "token": self.token
                }
        response = self.app.get('/bucketlists', data=form)
        self.assertEqual(response.status_code, 200)

    @skip
    def test_get_bucketlists_successfully_content(self):
        response = self.app.get('/bucketlists', data={
            "token": self.token
            })
        self.assertEqual(response.status_code, 200)
        self.assertTrue("first bucket" in response.data.decode('utf-8').lower())
        self.assertTrue("second bucket" in response.data.decode('utf-8').lower())

    @skip
    def test_get_bucketlist_no_token(self):
        response = self.app.get('/bucketlists', data=None)
        self.assertEqua(response.status_code, 403)

    @skip
    def test_get_bucketlist_no_token_content(self):
        response = self.app.get('/bucketlists', data=None)
        self.assertEqual(response.status_code, 403)
        self.assertTrue("token required" in response.data.decode('utf-8').lower())


    def tearDown(self):
        db.drop_all()
