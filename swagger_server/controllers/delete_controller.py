import connexion
import six

from swagger_server.models.note import Note  # noqa: E501
from swagger_server import util

import pymongo

from bson import json_util
import json


def delete_note(note_id):  # noqa: E501
    """Delete note by id

    Delete note by id. # noqa: E501

    :param id: Id of note to update.
    :type id: int

    :rtype: List[Note]
    """

    client = pymongo.MongoClient("localhost", 27017)

    db = client.test

    db.notes

    if note_id:
        users = db.users.find({'username': connexion.context['token_info']['username']})
        for user in users:
            delete = {'id': str(note_id), 'userid': user['id']}
            db.notes.delete_one(delete)
            return 'success'
    return 'failed'
