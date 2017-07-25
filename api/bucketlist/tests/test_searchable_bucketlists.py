#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_searchable_bucketlists.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 24.07.2017
# Last Modified: 24.07.2017

from .base import BaseTestCase
import json


class SearchTestCase(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp()
        # create the bucketlists
        bucketlists = ["One", "Two", "Three", "Four", "Five", "Six"]
        for name in bucketlists:
            self.app.post('/bucketlists', data={
                "title": name,
                "description": "lorem ipsum dor description",
                }, headers={"token": self.token})

    def test_search_db_successfully(self):
        response = self.app.get("/bucketlists", data={
            "q": "one",
            }, headers={"token": self.token})
        self.assertEqual(response.status_code, 200)

    def test_search_db_successfully_content(self):
        response = self.app.get("/bucketlists", data={
            "q": "one",
            }, headers={"token": self.token})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(json.loads(response.data.decode('utf-8'))['bucketlists']), 1)

    def test_search_db_kewords_content(self):
        response = self.app.get("/bucketlists", data={
            "q": 't',
            }, headers={"token": self.token})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(json.loads(response.data.decode('utf-8'))['bucketlists']), 2)

    def test_search_not_found(self):
        response = self.app.get("/bucketlists", data={
            "q": "lslsliehfie",
            }, headers={"token": self.token})
        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            "no bucketlist found" in response.data.decode('utf-8').lower())
