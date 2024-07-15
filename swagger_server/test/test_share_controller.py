# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestShareController(BaseTestCase):
    """ShareController integration test stubs"""

    def test_share_note(self):
        """Test case for share_note

        Share note by id to user by id
        """
        response = self.client.open(
            '/api//share/{noteId}/{userId}'.format(note_id=789, user_id=789),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
