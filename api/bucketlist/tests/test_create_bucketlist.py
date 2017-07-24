#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_create_bucketlist.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 17.07.2017
# Last Modified: 17.07.2017

from .base import BaseTestCase


class CreateBucketList(BaseTestCase):

    def test_create_bucketlist_successfully(self):
        form = {
            "title": "My list",
            "description": "lorem ipsum blah blah",
            "token": self.token
        }
        response = self.app.post('/bucketlists', data=form)
        self.assertEqual(response.status_code, 200)

    def test_create_bucketlist_duplicate(self):
        form = {
            "title": "My list",
            "description": "lorem ipsum blah blah",
            "token": self.token
        }
        response = self.app.post('/bucketlists', data=form)
        self.assertEqual(response.status_code, 200)

        dup_response = self.app.post('/bucketlists', data=form)
        self.assertEqual(dup_response.status_code, 200)
        self.assertTrue(
            "list my list already exists" in dup_response.data.decode('utf-8').lower())

    def test_create_bucketlist_no_token(self):
        form = {
            "title": "My another list",
            "description": "lorem ipsum dor yeah yeah"
        }
        response = self.app.post('/bucketlists', data=form)
        self.assertEqual(response.status_code, 403)

    def test_create_bucketlist_successfully_message(self):
        form = {
            "title": "My list",
            "description": "lorem ipsum blah blah",
            "token": self.token
        }
        response = self.app.post('/bucketlists', data=form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "list my list created successfully" in response.data.decode('utf-8').lower())

    def test_create_bucketlist_no_token_message(self):
        form = {
            "title": "My another list",
            "description": "lorem ipsum dor yeah yeah"
        }
        response = self.app.post('/bucketlists', data=form)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            "token required" in response.data.decode('utf-8').lower())
