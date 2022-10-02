import unittest

from pycouchdb import Server

import couchdblink.server_functions as sfn
from base import TestCaseBase


class TestGetCouchdbConnection(TestCaseBase):
    def test_connection_no_args(self):
        s = sfn.get_couchdb_connection()
        self.assertIsInstance(s, Server)
        s.resource.session.close()

    def test_connection_no_login(self):
        s = sfn.get_couchdb_connection()
        self.assertIsInstance(s, Server)
        s.resource.session.close()


if __name__ == "__main__":
    unittest.main()
