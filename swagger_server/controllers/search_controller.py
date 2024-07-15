import connexion
import six

from swagger_server.models.note import Note  # noqa: E501
from swagger_server import util

import pymongo

from bson import json_util
import json


def search_notes(body):  # noqa: E501
    """Search notes by text

    Search notes by text. # noqa: E501

    :param _str: Query string
    :type _str: str

    :rtype: List[Note]
    """

    client = pymongo.MongoClient("localhost", 27017)

    db = client.test

    db.notes

    if connexion.request.is_json:
        body = Note.from_dict(connexion.request.get_json())  # noqa: E501
        json_body = body.to_dict()
        users = db.users.find({'username': connexion.context['token_info']['username']})
        for user in users:
            records = db.notes.find({'userid': user['id']})
            for record in records:
                record_dict = json.loads(json_util.dumps(record))
                if json_body['note'] in record_dict['note']:
                    return record_dict
    return 'failed'

