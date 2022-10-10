import unittest

from pycouchdb import client

import couchdblink.server_functions as sfn
from base import TestCaseBase, TestCaseWithDb


class TestGetCouchdbConnection(TestCaseBase):
    def test_connection_no_args(self):
        s = sfn.get_couchdb_connection()
        self.assertIsInstance(s, client.Server)
        sfn.close(s)

    def test_connection_no_login(self):
        s = sfn.get_couchdb_connection()
        self.assertIsInstance(s, client.Server)
        sfn.close(s)


class TestMakeDb(TestCaseBase):
    def setUp(self):
        self.server = sfn.get_couchdb_connection()
        self.test_name = self.random_str(16, prefix="test")

    def test_make_db(self):
        db = sfn.get_make_db(self.server, self.test_name)
        self.assertIsInstance(db, client.Database)

    def tearDown(self):
        self.server.delete(self.test_name)
        self.server.resource.session.close()


class TestGetDb(TestCaseWithDb):
    def test_get_db(self):
        db = sfn.get_make_db(self.server, self.test_name)
        self.assertIsInstance(db, client.Database)


if __name__ == "__main__":
    unittest.main()
