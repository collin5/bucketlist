#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: api/bucketlist/views.py
# Author: Collins Abitekaniza <abtcolns@gmail.com>
# Date: 10.07.2017
# Last Modified: 10.07.2017

from api.app import app, db
from flask import request, jsonify
from api.auth.security.decorators import require_fields, token_required
from .models import Bucketlist, BucketItem
from datetime import datetime
import jwt


class Static:

    @staticmethod
    def decode_token(request):
        return jwt.decode(request.form['token'], app.secret_key, algorithims=['HS256'])


@app.route("/bucketlists", methods=['POST'])
@token_required
@require_fields('title', 'description')
def bucketlists():
    title, desc = request.form['title'], request.form['description']
    payload = Static.decode_token(request)

    if not Bucketlist.query.filter_by(title=title.lower()).first():
        bucket = Bucketlist(title=title.lower(),
                            description=desc, user_id=payload['id'])
        db.session.add(bucket)
        db.session.commit()
        return "list {} created successfully".format(title)
    else:
        return "list {} already exists".format(title)


@app.route("/bucketlists", methods=['GET'])
@app.route("/bucketlists/<int:id>", methods=['GET'])
@token_required
def get_bucketlists(id=None):
    """Gets bucket list from database"""
    payload = Static.decode_token(request)
    query = Bucketlist.query.filter_by(user_id=payload['id']).all(
    ) if not id else Bucketlist.query.filter_by(user_id=payload['id'], id=id).all()
    if not query:
        return "No bucketlist found", 404
    result = {}
    for obj in query:
        result[obj.id] = {
            "title": obj.title,
            "description": obj.description,
            "created on": obj.time_stamp
        }
    return jsonify(result)


@app.route("/bucketlists/<int:id>", methods=['PUT', 'DELETE'])
@token_required
def update_bucketlist(id):
    payload = Static.decode_token(request)

    if request.method == 'PUT':
        # we are to only edit submitted fileds, else do nothing
        title, desc = request.form.get(
            'title', None), request.form.get('description', None)
        if not title and not desc:
            return "Nothing to change, all fields are null"

        '''Now get bucket list from database
        Also get only if bucketlist belongs to this user'''
        obj = Bucketlist.query.filter_by(user_id=payload['id'], id=id).first()
        if not obj:
            return "Bucketlist not found", 404
        else:
            if title:
                obj.title = title
            if desc:
                obj.description = desc
            db.session.commit()
            return "Bucketlist updated successfully"
    if request.method == 'DELETE':
        if not Bucketlist.query.filter_by(user_id=payload['id'], id=id).first():
            return "Bucketlist not found", 404
        else:
            Bucketlist.query.filter_by(user_id=payload['id'], id=id).delete()
            db.session.commit()
            return "Bucketlist deleted successfully"


@app.route("/bucketlists/<int:id>/items", methods=['POST'])
@token_required
@require_fields('title', 'notes', 'deadline')
def bucket_items(id):
    title, notes = request.form['title'], request.form['notes']
    deadline = datetime.strptime(request.form['deadline'], "%d-%b-%Y")

    payload = Static.decode_token(request)

    # get bucket list that belongs to user
    bucketlist = Bucketlist.query.filter_by(
        user_id=payload['id'], id=id).first()

    if not bucketlist:
        return "Bucketlist not found", 404
    else:
        item = BucketItem(title=title, notes=notes,
                          deadline=deadline, bucketlist_id=bucketlist.id,user_id=payload['id'])
        db.session.add(item)
        db.session.commit()
        return "Item added successfully"


@app.route("/bucketlists/<int:id>/items", methods=['GET'])
@app.route("/bucketlists/<int:id>/items/<int:item_id>", methods=['GET'])
@token_required
def get_bucket_items(id, item_id=None):
    payload = Static.decode_token(request)
    if not Bucketlist.query.filter_by(user_id=payload['id'], id=id).first():
        return "Bucketlist not found", 404
    else:
        query = BucketItem.query.filter_by(user_id=payload['id'], bucketlist_id=id, id=item_id).all(
        ) if item_id else BucketItem.query.filter_by(user_id=payload['id'], bucketlist_id=id).all()

        if not query:
            return "Bucketitem not found", 404
        else:
            result = {}
            for item in query:
                result[item.id] = {
                    "title": item.title,
                    "notes": item.notes,
                    "deadline": item.deadline,
                    "created_on": item.time_stamp
                }
            return jsonify(result)


@app.route("/bucketlists/<int:id>/items/<int:item_id>", methods=['PUT', 'DELETE'])
def update_bucket_items(id, item_id):
    pass
