from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""

import pymongo
import bcrypt

import json

def check_api_key(api_key, required_scopes):
    if api_key:
        client = pymongo.MongoClient("localhost", 27017)

        db = client.test

        db.users

        credentials = json.loads(api_key)
        username = [*credentials][0]
        password = [*credentials.values()][0]
        user = db.users.find_one({'username': username})
        if user and bcrypt.checkpw(bytes(password, 'utf-8'), user['password']):
            return {"username": username}


