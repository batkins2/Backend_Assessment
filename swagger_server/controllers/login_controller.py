import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

import pymongo
import bcrypt

def login(body):  # noqa: E501
    """log into an account

    Log into an account # noqa: E501

    :param body: Log into an account
    :type body: dict | bytes

    :rtype: None
    """

    client = pymongo.MongoClient("localhost", 27017)

    db = client.test

    db.users

    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        json = body.to_dict()
        user = db.users.find_one({'username': json['username']})
        if user and bcrypt.checkpw(bytes(json['password'], 'utf-8'), user['password']):
            return 'success'
    return 'failed'
