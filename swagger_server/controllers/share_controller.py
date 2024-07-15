import connexion
import six

from swagger_server import util

import pymongo

from bson import json_util
import json

import re

def share_note(note_id, user_id):  # noqa: E501
    """Share note by id to user by id

    Share note by id to user by id. # noqa: E501

    :param note_id: Id of note to share.
    :type note_id: int
    :param user_id: Id of user to send note.
    :type user_id: int

    :rtype: None
    """
    client = pymongo.MongoClient("localhost", 27017)

    db = client.test

    db.notes

    if note_id and user_id:
        records = db.notes.find({'id': str(note_id)})
        for record in records:
            record_json = json.loads(json_util.dumps(record))
            this_user = db.users.find({'username': connexion.context['token_info']['username']})
            that_user = db.users.find({'id': str(user_id)})
            if this_user and that_user:
                for user in that_user:
                    user_json = json.loads(json_util.dumps(user))
                    record_json['userid'] = user_json['id']
                    del record_json['_id']
                    new_id = db.notes.insert_one(record_json).inserted_id
                    new_records = db.notes.find({'_id': new_id})
                    for new_record in new_records:
                        new_record_json = json.loads(json_util.dumps(new_record))
                        id = re.sub('\D', '', new_record_json['_id']['$oid'])
                        db.notes.update({'_id': new_id}, {'$set': {'id': id}})
                        return id
                    return 'failed (2)'
                return 'failed (1)'
            return 'failed (0)'
        return 'failed (-1)'
    return 'failed'

