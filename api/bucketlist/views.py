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
        return jwt.decode(request.headers['token'], app.secret_key, algorithims=['HS256'])


@app.route("/bucketlists", methods=['POST'])
@token_required
@require_fields('title', 'description')
def bucketlists():
    """Endpoint for adding bucketlists, call with token included in header
---
       tags:
        - Bucketlists
       parameters:
        - name: token
          in: headers
          type: string
          required: true
        - name: title
          in: body
          type: string
          required: true
        - name: description
          in: body
          type: string
          required: true
         """

    title, desc = request.form['title'], request.form['description']
    payload = Static.decode_token(request)

    if not Bucketlist.query.filter_by(title=title.lower()).first():
        bucket = Bucketlist(title=title.lower(),
                            description=desc, user_id=payload['id'])
        db.session.add(bucket)
        db.session.commit()
        return jsonify({
            "success_msg": "list {} created successfully".format(title)
        })
    else:
        return jsonify({
            "error_msg": "list {} already exists".format(title)
        })


@app.route("/bucketlists", methods=['GET'])
@app.route("/bucketlists/<int:id>", methods=['GET'])
@token_required
def get_bucketlists(id=None):
    """Endpoint for getting bucketlists, call with token included in header
---
       tags:
        - Bucketlists
       parameters:
        - name: token
          in: headers
          type: string
          required: true
        - name: id
          in: path
          type: int
          required: false
         """
    payload = Static.decode_token(request)
    limit, offset = request.args.get(
        'limit', None), request.args.get('offset', None)
    search = request.args.get('q', None)

    query = Bucketlist.query.filter_by(
        user_id=payload['id']) if not id else Bucketlist.query.filter_by(user_id=payload['id'], id=id)
    if offset:
        query = query.offset(offset)
    if limit:
        query = query.limit(limit)
    if search:
        query = query.filter(Bucketlist.title.like("%{}%".format(search.lower())))
    query = query.all()
    if not query:
        return jsonify({
            "error_msg": "No bucketlist found"
        }), 404
    result = {"bucketlists": {}}
    for obj in query:
        result["bucketlists"][obj.id] = {
            "title": obj.title,
            "description": obj.description,
            "created_on": obj.time_stamp
        }
    return jsonify(result)


@app.route("/bucketlists/<int:id>", methods=['PUT', 'DELETE'])
@token_required
def update_bucketlist(id):
    """Endpoint for updating a bucketlist, call with token included in header
---
       tags:
        - Bucketlists
       parameters:
        - name: id
          in: path
          type: int
          required: true
        - name: title
          in: body
          type: string
        - name: description
          in: body
          type: string
         """

    payload = Static.decode_token(request)

    if request.method == 'PUT':
        # we are to only edit submitted fileds, else do nothing
        title, desc = request.form.get(
            'title', None), request.form.get('description', None)
        if not title and not desc:
            return jsonify({
                "error_msg": "Nothing to change, all fields are null"
            })

        '''Now get bucket list from database
        Also get only if bucketlist belongs to this user'''
        obj = Bucketlist.query.filter_by(user_id=payload['id'], id=id).first()
        if not obj:
            return jsonify({
                "error_msg": "Bucketlist not found"
            }), 404
        else:
            if title:
                obj.title = title
            if desc:
                obj.description = desc
            db.session.commit()
            return jsonify({
                "success_msg": "Bucketlist updated successfully"
            })
    if request.method == 'DELETE':
        if not Bucketlist.query.filter_by(user_id=payload['id'], id=id).first():
            return jsonify({
                "error_msg": "Bucketlist not found"
            }), 404
        else:
            Bucketlist.query.filter_by(user_id=payload['id'], id=id).delete()
            db.session.commit()
            return jsonify({
                "success_msg": "Bucketlist deleted successfully"
            })


@app.route("/bucketlists/<int:id>/items", methods=['POST'])
@token_required
@require_fields('title', 'notes', 'deadline')
def bucket_items(id):
    """Endpoint for adding bucketlist item, call with token included in header
---
       tags:
        - Bucketlist items
       parameters:
        - name: id
          in: path
          required: true
          type: int
        - name: title
          in: body
          required: true
          type: string
        - name: notes
          in: body
          required: true
          type: string
        - name: deadline
          type: string
          description: "Use format dd-M-Y"
          required: true
         """

    title, notes = request.form['title'], request.form['notes']
    try:
        deadline = datetime.strptime(request.form['deadline'], "%d-%b-%Y")
    except Exception as ex:
        return jsonify({
            "error_msg": "Ivalid date format please, use dd-M-Y"
            })

    payload = Static.decode_token(request)

    # get bucket list that belongs to user
    bucketlist = Bucketlist.query.filter_by(
        user_id=payload['id'], id=id).first()

    if not bucketlist:
        return jsonify({
            "error_msg": "Bucketlist not found"
        }), 404
    else:
        item = BucketItem(title=title, notes=notes,
                          deadline=deadline, bucketlist_id=bucketlist.id, user_id=payload['id'])
        db.session.add(item)
        db.session.commit()
        return jsonify({
            "success_msg": "Item added successfully"
        })


@app.route("/bucketlists/<int:id>/items", methods=['GET'])
@app.route("/bucketlists/<int:id>/items/<int:item_id>", methods=['GET'])
@token_required
def get_bucket_items(id, item_id=None):
    """Endpoint for getting bucketlist items, call with token included in header
---
       tags:
        - Bucketlist items
       parameters:
        - name: id
          type: int
          required: true
          in: path
        - name: item_id
          type: int
          required: false
          in: path
         """

    payload = Static.decode_token(request)
    if not Bucketlist.query.filter_by(user_id=payload['id'], id=id).first():
        return jsonify({
            "error_msg": "Bucketlist not found"
        }), 404
    else:
        query = BucketItem.query.filter_by(user_id=payload['id'], bucketlist_id=id, id=item_id).all(
        ) if item_id else BucketItem.query.filter_by(user_id=payload['id'], bucketlist_id=id).all()

        if not query:
            return jsonify({
                "error_msg": "Bucketitem not found"
            }), 404
        else:
            result = {"bucketlist": id, "items": {}}
            for item in query:
                result["items"][item.id] = {
                    "title": item.title,
                    "notes": item.notes,
                    "deadline": item.deadline,
                    "created_on": item.time_stamp
                }
            return jsonify(result)


@app.route("/bucketlists/<int:id>/items/<int:item_id>", methods=['PUT', 'DELETE'])
@token_required
def update_bucket_items(id, item_id):
    """Endpoint for updating bucketlist item, call with token included in header
---
       tags:
        - Bucketlist items
       parameters:
        - name: id
          in: path
          required: true
          type: int
        - name: item_id
          required: true
          type: int
          in: path
        - name: title
          in: body
          type: string
        - name: notes
          in: body
          type: string
        - name: deadline
          type: string
          description: "Use format dd-M-Y"

         """
         
    payload = Static.decode_token(request)

    # first check if bucketlist exists
    if not Bucketlist.query.filter_by(user_id=payload['id'], id=id).first():
        return jsonify({
            "error_msg": "Bucketlist not found"
        }), 404
    else:
        item = BucketItem.query.filter_by(
            user_id=payload['id'], id=item_id, bucketlist_id=id).first()
        # Also check if bucket item exists
        if not item:
            return jsonify({
                "error_msg": "Bucketitem not found"
            }), 404

        if request.method == 'PUT':
            title, notes = request.form.get(
                'title', None), request.form.get('notes', None)
            deadline = request.form.get('deadline', None)

            if not title and not notes and not deadline:
                return jsonify({
                    "error_msg": "Nothing to change"
                })
            else:
                if title:
                    item.title = title
                if notes:
                    item.notes = notes
                if deadline:
                    item.deadline = deadline
                db.session.commit()
                return jsonify({
                    "success_msg": "Bucketitem successfully updated"
                })
        if request.method == 'DELETE':
            BucketItem.query.filter_by(
                user_id=payload['id'], id=item_id, bucketlist_id=id).delete()
            db.session.commit()
            return jsonify({
                "success_msg": "Bucketitem successfully deleted"
            })
