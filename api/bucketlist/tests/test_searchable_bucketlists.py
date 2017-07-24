#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_searchable_bucketlists.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 24.07.2017
# Last Modified: 24.07.2017

from .base import BaseTestCase
import json
from unittest import skip


class SearchTestCase(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp()
        # create the bucketlists
        bucketlists = ["One", "Two", "Three", "Four", "Five", "Six"]
        for name in bucketlists:
            self.app.post('/bucketlists', data={
                "name": name,
                "description": "lorem ipsum dor description",
                "token": self.token
            })

    @skip
    def test_search_db_successfully(self):
        response = self.bucketlists.get("/bucketlists", data={
            "q": "one",
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)

    @skip
    def test_search_db_successfully_content(self):
        response = self.bucketlists.get("/bucketlists", data={
            "q": "one",
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(json.loads(response.data.decode('utf-8'))['bucketlists']), 1)

    @skip
    def test_search_db_kewords_content(self):
        response = self.bucketlists.get("/bucketlists", data={
            "q": 't',
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(json.loads(response.data.decode('utf-8'))['bucketlists']), 2)

    @skip
    def test_search_not_found(self):
        response = self.bucketlists.get("/bucketlists", data={
            "q": "lslsliehfie",
            "token": self.token
        })
        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            "bucketlist not found" in response.data.decode('utf-8'))
