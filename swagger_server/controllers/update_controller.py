import connexion
import six

from swagger_server.models.note import Note  # noqa: E501
from swagger_server import util

import pymongo

from bson import json_util
import json


def update_note(note_id, body):  # noqa: E501
    """Update note by id

    Update note by id. # noqa: E501

    :param id: Id of note to update.
    :type id: int

    :rtype: List[Note]
    """
    client = pymongo.MongoClient("localhost", 27017)

    db = client.test

    db.notes

    if note_id:
        body = Note.from_dict(connexion.request.get_json())  # noqa: E501
        json_body = body.to_dict()
        users = db.users.find({'username': connexion.context['token_info']['username']})
        for user in users:
            update = {'id': str(note_id), 'userid': user['id']}
            db.notes.update(update, {'$set': {'note': json_body['note'], 'name': json_body['name']}})
            records = db.notes.find(update)
            for record in records:
                return json.loads(json_util.dumps(record))

    return 'failed'
