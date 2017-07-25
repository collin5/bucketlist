#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/tests/test_update_bucketlist.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 19.07.2017
# Last Modified: 19.07.2017
from .base import BaseTestCase


class UpdateBucketlistTestCase(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp()
        # create a bucket list for testing
        self.app.post('/bucketlists', data={
            "title": "Awesome, beautiful list",
            "description": "lorem ipsum blah blah ...",
            }, headers={"token": self.token})

    def test_update_bucketlist_successfully(self):
        initial_request = self.app.get('/bucketlists', headers={
            "token": self.token
        })
        # first confirm initial name
        self.assertEqual(initial_request.status_code, 200)
        self.assertTrue(
            "awesome, beautiful list" in initial_request.data.decode('utf-8').lower())

        # now send update request
        update_request = self.app.put("/bucketlists/1", data={
            "title": "Edited title over here",
            "description": "hohoohohohohohohohohoho",
            }, headers={"token": self.token})
        self.assertEqual(update_request.status_code, 200)

        final_request = self.app.get('/bucketlists/1', headers={
            "token": self.token
        })
        self.assertEqual(final_request.status_code, 200)
        self.assertTrue(
            "edited title over here" in final_request.data.decode('utf-8').lower())

    def test_update_bucketlist_successfully_content(self):
        update_request = self.app.put("/bucketlists/1", data={
            "title": "Again edited our title, what ?",
            "description": "lorem blah oh my god",
            }, headers={"token": self.token})
        self.assertEqual(update_request.status_code, 200)
        self.assertTrue(
            "bucketlist updated successfully" in update_request.data.decode('utf-8').lower())

    def test_update_bucketlist_no_form(self):
        update_request = self.app.put('/bucketlists/1', headers={
            'token': self.token
        })
        self.assertEqual(update_request.status_code, 200)
        self.assertTrue(
            "nothing to change" in update_request.data.decode('utf-8').lower())

    def test_update_bucketlist_index_out_of_range(self):
        update_request = self.app.put("/bucketlists/49", data={
            "title": "Now this is not good",
            "description": "Why trying to overflow bucket",
            }, headers={"token": self.token})
        self.assertEqual(update_request.status_code, 404)
        self.assertTrue("bucketlist not found")

    def test_update_bucketlist_no_token(self):
        update_request = self.app.put("/bucketlists/1", data={
            "title": "Ok let me try without id",
            "description": "evil minds dor ipsum"
        })
        self.assertEqual(update_request.status_code, 403)
        self.assertTrue(
            "token required" in update_request.data.decode('utf-8').lower())
