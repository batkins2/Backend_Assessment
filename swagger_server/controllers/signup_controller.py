import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

import pymongo
import bcrypt

from bson import json_util
import json

import re

def sign_up(body):  # noqa: E501
    """Sign up for an account

    Sign up for an account # noqa: E501

    :param body: Sign up for an account
    :type body: dict | bytes

    :rtype: None
    """

    client = pymongo.MongoClient("localhost", 27017)

    db = client.test

    db.users

    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        json_body = body.to_dict()
        if json_body['password'] and json_body['username'] and json_body['email']:
            json_body['password'] = bcrypt.hashpw(bytes(json_body['password'], 'utf-8'), bcrypt.gensalt())
            record_id = db.users.insert_one(json_body).inserted_id
            records = db.users.find({'_id': record_id})
            for record in records:
                id = re.sub('\D', '', json.loads(json_util.dumps(record))['_id']['$oid'])
                db.users.update({'_id': record_id}, {'$set': {'id': id}})
                return id
    return 'failed'
