#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/views.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import app

@app.route("/bucketlists", methods=['POST', 'GET'])
def bucketlists():
    pass


@app.route("/bucketlists/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def bucketlists(id):
    pass

@app.route("/bucketlists/<int:id>/items/", methods=['POST'])
def bucketlist_items(id):
    pass


@app.route("/bucketlists/<int:id>/items/<int:item_id>", methods=['PUT', 'DELETE'])
def bucketlist_items(id, item_id):
    pass


