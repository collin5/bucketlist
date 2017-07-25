#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_get_items.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 20.07.2017
# Last Modified: 20.07.2017

from .base import BaseTestCase


class GetItemTestCase(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp()

        self.app.post('/bucketlists', data={
            "title": "The bucket man",
            "description": "this is a decription",
            }, headers={"token": self.token})

        # add bucket item for test case
        self.app.post('/bucketlists/1/items', data={
            "title": "item",
            "notes": "lorem ipsum dor ...",
            "deadline": "01-Feb-2019",
            }, headers={"token": self.token})

    def test_get_bucket_item_succcessfully(self):
        response = self.app.get('/bucketlists/1/items', headers={
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)

    def test_get_bucket_item_succcessfully_content(self):
        response = self.app.get('/bucketlists/1/items', headers={
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue("item" in response.data.decode('utf-8').lower())

    def test_get_bucket_item_list_out_of_range(self):
        response = self.app.get('/bucketlists/2/items', headers={
            "token": self.token
        })
        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            "bucketlist not found" in response.data.decode('utf-8').lower())

    def test_get_bucket_item_with_id_successfully(self):
        response = self.app.get('/bucketlists/1/items/1', headers={
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue("item" in response.data.decode('utf-8').lower())

    def test_get_bucket_item_item_out_range(self):
        response = self.app.get('/bucketlists/1/items/2', headers={
            "token": self.token
        })
        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            "item not found" in response.data.decode('utf-8').lower())

    def test_get_bucket_items_no_token(self):
        response = self.app.get('/bucketlists/1/items', data=None)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            "token required" in response.data.decode('utf-8').lower())
