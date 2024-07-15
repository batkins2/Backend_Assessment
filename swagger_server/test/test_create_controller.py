# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.note import Note  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCreateController(BaseTestCase):
    """CreateController integration test stubs"""

    def test_create_note(self):
        """Test case for create_note

        Create a note
        """
        body = Note()
        response = self.client.open(
            '/api//create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
