import connexion
import six

from swagger_server.models.note import Note  # noqa: E501
from swagger_server import util

import pymongo

from bson import json_util
import json

def get_note(note_id):  # noqa: E501
    """Get note by id

    Get note by id # noqa: E501

    :param id: Id for note
    :type id: int

    :rtype: List[Note]
    """

    client = pymongo.MongoClient("localhost", 27017)

    db = client.test

    db.notes

    if note_id:
        # return note_id
        users = db.users.find({'username': connexion.context['token_info']['username']})
        for user in users:
            records = db.notes.find({'id': str(note_id), 'userid': user['id']})
            for record in records:
                return json.loads(json_util.dumps(record))

    return 'failed'
