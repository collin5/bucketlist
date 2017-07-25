#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_paginate_bucketlists.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 24.07.2017
# Last Modified: 24.07.2017

from .base import BaseTestCase
import json


class PaginationTestCase(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp()
        # first add bucketlists
        bucketlists = ["list 1", "list 2", "list 3", "list 4", "list 5"]
        for name in bucketlists:
            self.app.post('/bucketlists', data={
                "title": name,
                "description": "lorem ipsum dor ...",
                }, headers={"token": self.token})

    def test_limit_successfully(self):
        response = self.app.get('/bucketlists?limit=2', headers={"token": self.token})
        self.assertEqual(response.status_code, 200)

    def test_limit_content(self):
        response = self.app.get('/bucketlists?limit=3', headers={"token": self.token})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(json.loads(response.data.decode('utf-8'))['bucketlists']), 3)

    def test_offset_successfully(self):
        response = self.app.get('/bucketlists?offset=2', data={
            "offset": 2,
            }, headers={"token": self.token})
        self.assertEqual(response.status_code, 200)

    def test_offset_content(self):
        response = self.app.get('/bucketlists?offset=2', headers={"token": self.token})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(json.loads(response.data.decode('utf-8'))['bucketlists']), 3)

    def test_limit_with_offset_successfully(self):
        response = self.app.get('/bucketlists?limit=4&offset=2', headers={"token": self.token})
        self.assertEqual(response.status_code, 200)

    def test_limit_with_offset_content(self):
        response = self.app.get('/bucketlists?limit=4&offset=2', headers={"token": self.token})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(json.loads(response.data.decode('utf-8'))['bucketlists']), 3)
