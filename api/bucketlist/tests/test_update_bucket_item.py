#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_update_bucket_item.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 20.07.2017
# Last Modified: 20.07.2017


from .base import BaseTestCase


class UpdateItemTestCase(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp()

        self.app.post('/bucketlists', data={
            "title": "list",
            "description": "this is the des",
            "token": self.token
        })

        self.app.post('/bucketlists/1/items', data={
            "title": "My awesome item",
            "notes": "lorem ipsum dor",
            "deadline": "01-Dec-3030",
            "token": self.token
        })

    def test_update_item_successfully(self):
        form = {
            "title": "New title for item",
            "notes": "now this is fun",
            "token": self.token
        }
        response = self.app.put('/bucketlists/1/items/1', data=form)
        self.assertEqual(response.status_code, 200)

    def test_update_item_successfully_content(self):
        form = {
            "title": "New title for item",
            "notes": "now this is fun",
            "token": self.token
        }
        response = self.app.put('/bucketlists/1/items/1', data=form)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'item successfully updated' in response.data.decode('utf-8').lower())

    def test_update_item_successfully_content_2(self):
        initial_item = self.app.get(
            '/bucketlists/1/items/1', data={"token": self.token})

        self.assertEqual(initial_item.status_code, 200)
        self.assertTrue(
            "my awesome item" in initial_item.data.decode('utf-8').lower())
        form = {
            "title": "New title for item",
            "notes": "now this is fun",
            "token": self.token
        }

        update_response = self.app.put('/bucketlists/1/items/1', data=form)
        self.assertEqual(update_response.status_code, 200)

        final_item = self.app.get(
            '/bucketlists/1/items/1', data={"token": self.token})
        self.assertTrue(
            "new title for item" in final_item.data.decode('utf-8').lower())

    def test_update_item_no_token(self):
        response = self.app.put('/bucketlists/1/items/1', data={
            "title": "My new awesome title"
        })
        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            "token required" in response.data.decode('utf-8').lower())

    def test_update_item_empty_form(self):
        response = self.app.put('/bucketlists/1/items/1', data={
            "token": self.token
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            "nothing to change" in response.data.decode('utf-8').lower())

    def test_update_item_bucketlist_out_of_range(self):
        response = self.app.put('/bucketlists/4/items/1', data={
            "title": "I love titles",
            "token": self.token
        })
        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            "bucketlist not found" in response.data.decode('utf-8').lower())

    def test_update_item_item_out_of_range(self):
        response = self.app.put('/bucketlists/1/items/345', data={
            "title": "Now this is obvious",
            "token": self.token
        })

        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            "bucketitem not found" in response.data.decode('utf-8').lower())
