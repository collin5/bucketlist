#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_delete_bucketlist.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 19.07.2017
# Last Modified: 19.07.2017

from api.app import app, db
from unittest import TestCase, skip


class DeleteBucketlistTestCase(TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.create_all()

        reg_form = {
            "username": "collins",
            "email": "collins@andela.com",
            "password": "v3rY5trongPa5SworD?"
        }
        self.app.post('/auth/register', data=reg_form)
        self.token = self.app.post('/auth/login', data={
            "username": "collins",
            "password": "v3rY5trongPa5SworD?"
        }).data.decode('utf-8')

        # our testing bucketlist
        self.app.post('/bucketlists', data={
            "title": "I'm a bucketlist",
            "description": "And i am awesome",
            "token": self.token
        })

    def test_delete_bucketlist_successfully(self):
        response = self.app.delete('/bucketlists/1', data={
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_bucketlist_successfully_message(self):
        response = self.app.delete('/bucketlists/1', data={
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'bucketlist deleted successfully' in response.data.decode('utf-8').lower())

    def test_delete_bucketlist_out_of_range(self):
        response = self.app.delete('/bucketlists/898', data={
            "token": self.token
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_bucketlist_out_of_range_message(self):
        response = self.app.delete('/bucketlists/7', data={
            "token": self.token
        })
        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            "bucketlist not found" in response.data.decode('utf-8').lower())

    def test_delete_bucketlist_no_token(self):
        response = self.app.delete('/bucketlists/1', data=None)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            "token required" in response.data.decode('utf-8').lower())

    def tearDown(self):
        db.drop_all()
