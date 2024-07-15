# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.note import Note  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUpdateController(BaseTestCase):
    """UpdateController integration test stubs"""

    def test_update_note(self):
        """Test case for update_note

        Update note by id
        """
        response = self.client.open(
            '/api//update/{id}'.format(id=789),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
