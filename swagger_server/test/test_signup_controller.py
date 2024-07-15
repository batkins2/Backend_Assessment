# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSignupController(BaseTestCase):
    """SignupController integration test stubs"""

    def test_sign_up(self):
        """Test case for sign_up

        Sign up for an account
        """
        body = User()
        response = self.client.open(
            '/api//auth/signup',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
