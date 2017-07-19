#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/views.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import app, db
from flask import request, jsonify 
from api.auth.security.decorators import require_fields, token_required
from .models import Bucketlist
import jwt


@app.route("/bucketlists", methods=['POST'])
@token_required
@require_fields('title', 'description')
def bucketlists():
    title, desc = request.form['title'], request.form['description']
    payload = jwt.decode(
        request.form['token'], app.secret_key, algorithims=['HS256'])

    if not Bucketlist.query.filter_by(title=title.lower()).first():
        bucket = Bucketlist(title=title.lower(),
                            description=desc, user_id=payload['id'])
        db.session.add(bucket)
        db.session.commit()
        return "list {} created successfully".format(title)
    else:
        return "list {} already exists".format(title)


@app.route("/bucketlists", methods=['GET'])
@app.route("/bucketlists/<int:id>", methods=['GET', 'PUT', 'DELETE'])
@token_required
def get_bucketlists(id=None):
    payload = jwt.decode(
        request.form['token'], app.secret_key, algorithims=['HS256'])
    if request.method == 'GET':
        query = Bucketlist.query.filter_by(user_id=payload['id']).all(
        ) if not id else Bucketlist.query.filter_by(user_id=payload['id'], id=id).all()
        if not query:
            return "No bucketlist found", 404
        result = {}
        for obj in query:
            result[obj.id] = [obj.title, obj.description, obj.time_stamp]
            
        return jsonify(result)
    else:
        return "Invalid request"


@app.route("/bucketlists/<int:id>/items/", methods=['POST'])
def bucketlist_items(id):
    pass


@app.route("/bucketlists/<int:id>/items/<int:item_id>", methods=['PUT', 'DELETE'])
def get_bucketlist_items(id, item_id):
    pass
