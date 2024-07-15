import connexion
import six

from swagger_server.models.note import Note  # noqa: E501
from swagger_server import util

import pymongo

from bson import json_util
import json

import re

def create_note(body):  # noqa: E501
    """Create a note

    Create a note # noqa: E501

    :param body: Create a note
    :type body: dict | bytes

    :rtype: Note
    """

    client = pymongo.MongoClient("localhost", 27017)

    db = client.test

    db.notes

    if connexion.request.is_json:
        body = Note.from_dict(connexion.request.get_json())  # noqa: E501
        json_body = body.to_dict()
        record_id = db.notes.insert_one(json_body).inserted_id
        records = db.notes.find({'_id': record_id})
        for record in records:
            id = re.sub('\D', '', json.loads(json_util.dumps(record))['_id']['$oid'])
            users = db.users.find({'username': connexion.context['token_info']['username']})
            for user in users:
                db.notes.update({'_id': record_id}, {'$set': {'id': id, 'userid': user['id']}})
                return id
    return 'failed'
