# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.note import Note  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDeleteController(BaseTestCase):
    """DeleteController integration test stubs"""

    def test_delete_note(self):
        """Test case for delete_note

        Delete note by id
        """
        response = self.client.open(
            '/api//delete/{id}'.format(id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
