#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_delete_item.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 20.07.2017
# Last Modified: 20.07.2017

from .base import BaseTestCase


class DeleteItemTestCase(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp()

        self.app.post('/bucketlists', data={
            "title": "I love todos",
            "description": "because I have to do the todos",
            }, headers={"token": self.token})

        self.app.post('/bucketlists/1/items', data={
            "title": "my nice item",
            "notes": "no notes for this item",
            "deadline": "01-Dec-3031",
            }, headers={"token": self.token})

    def test_delete_item_successfully(self):
        response = self.app.delete('/bucketlists/1/items/1', headers={
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_item_successfully_message(self):
        response = self.app.delete('/bucketlists/1/items/1', headers={
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "item successfully deleted" in response.data.decode('utf-8').lower())

    def test_delete_item_no_token(self):
        response = self.app.delete('/bucketlists/1/items/1', data=None)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            "token required" in response.data.decode('utf-8').lower())

    def test_delete_item_bucketlist_out_of_range(self):
        response = self.app.delete('/bucketlists/4/items/1', headers={
            "token": self.token
        })
        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            "bucketlist not found" in response.data.decode('utf-8').lower())

    def test_dlete_item_our_of_range(self):
        response = self.app.delete('/bucketlists/1/items/3', headers={
            "token": self.token
        })

        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            "item not found" in response.data.decode('utf-8').lower())
