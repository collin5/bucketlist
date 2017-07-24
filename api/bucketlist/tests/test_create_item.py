#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_items/test_create_item.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 19.07.2017
# Last Modified: 19.07.2017

from .base import BaseTestCase


class CreateItemTestCase(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp()
        # create bucketlist for the test
        self.app.post('/bucketlists', data={
            "title": "Here comes the bucketlist",
            "description": "with a description",
            "token": self.token
        })

    def test_create_bucketlist_item_successfully(self):
        form = {
            "title": "My awesome bucket item",
            "notes": "lorem ipsum dor ...",
            "deadline": "01-Jan-2018",
            "token": self.token
        }
        response = self.app.post('bucketlists/1/items', data=form)
        self.assertEqual(response.status_code, 200)

    def test_create_bucketlist_item_successfully_message(self):
        form = {
            "title": "My awesome bucket item",
            "notes": "lorem ipsum dor ...",
            "deadline": "01-Jan-2018",
            "token": self.token
        }
        response = self.app.post('bucketlists/1/items', data=form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'item added successfully' in response.data.decode('utf-8').lower())

    def test_create_bucketlist_item_out_of_range_bucketlist(self):
        form = {
            "title": "My awesome bucket item",
            "notes": "lorem ipsum dor ...",
            "deadline": "01-Jan-2018",
            "token": self.token
        }
        response = self.app.post('/bucketlists/4/items', data=form)
        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            "bucketlist not found" in response.data.decode('utf-8').lower())

    def test_create_bucketlist_item_no_token(self):
        form = {
            "title": "Evil item",
            "notes": "lorem ipsum dor ..",
            "deadline": "01-Jan-2018",
        }
        response = self.app.post('/bucketlists/1/items', data=form)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            "token required" in response.data.decode('utf-8').lower())

    def test_create_bucketlist_item_empty_form(self):
        response = self.app.post('/bucketlists/1/items', data={
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "please fill all fields" in response.data.decode('utf-8').lower())
