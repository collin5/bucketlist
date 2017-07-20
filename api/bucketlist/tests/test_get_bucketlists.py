#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_get_bucketlists.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 18.07.2017
# Last Modified: 18.07.2017

from api.app import app, db
from unittest import TestCase, skip

class GetBucketlistsTestCase(TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.create_all()
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
            }).data.decode('utf-8')
        # Add bucket list
        first_bucket = {
                "title": "First bucket",
                "description": "lorem ipsum blah blah ",
                "token": self.token
                }
        second_bucket = {
                "title": "Second bucket",
                "description": "lorem from second bucket is awesome",
                "token": self.token
                }
        self.app.post('/bucketlists', data=first_bucket)
        self.app.post('/bucketlists', data=second_bucket)
        

    def test_get_bucketlist_successfully(self):
        form = {
                "token": self.token
                }
        response = self.app.get('/bucketlists', data=form)
        self.assertEqual(response.status_code, 200)

    def test_get_bucketlists_successfully_content(self):
        response = self.app.get('/bucketlists', data={
            "token": self.token
            })
        self.assertEqual(response.status_code, 200)
        self.assertTrue("first bucket" in response.data.decode('utf-8').lower())
        self.assertTrue("second bucket" in response.data.decode('utf-8').lower())

    def test_get_single_bucketlist_successfully(self):
        form = {
                "token": self.token
                }
        response = self.app.get('/bucketlists/1', data=form)
        self.assertEqual(response.status_code, 200)

    def test_get_single_bucketlist_successfully_content(self):
        form = {
                "token": self.token
                }
        response = self.app.get('/bucketlists/2', data=form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('second' in response.data.decode('utf-8').lower())

    def test_get_bucketlist_out_of_range(self):
        form = {
                "token": self.token
                }
        response = self.app.get('/bucketlists/37', data=form)
        self.assertEqual(response.status_code, 404)
        self.assertTrue('no bucketlist found' in response.data.decode('utf-8').lower())


    def test_get_bucketlist_no_token(self):
        response = self.app.get('/bucketlists', data=None)
        self.assertEqual(response.status_code, 403)

    def test_get_bucketlist_no_token_content(self):
        response = self.app.get('/bucketlists', data=None)
        self.assertEqual(response.status_code, 403)
        self.assertTrue("token required" in response.data.decode('utf-8').lower())


    def tearDown(self):
        db.drop_all()
