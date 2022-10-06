import unittest

from pycouchdb import client

import couchdblink.server_functions as sfn
from base import TestCaseBase


class TestGetCouchdbConnection(TestCaseBase):
    def test_connection_no_args(self):
        s = sfn.get_couchdb_connection()
        self.assertIsInstance(s, client.Server)
        s.resource.session.close()

    def test_connection_no_login(self):
        s = sfn.get_couchdb_connection()
        self.assertIsInstance(s, client.Server)
        s.resource.session.close()


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


class TestGetDb(TestCaseBase):
    def setUp(self):
        self.server = sfn.get_couchdb_connection()
        self.test_name = self.random_str(16, prefix="test")
        self.server.create(self.test_name)

    def test_get_db(self):
        db = sfn.get_make_db(self.server, self.test_name)
        self.assertIsInstance(db, client.Database)

    def tearDown(self):
        self.server.delete(self.test_name)
        self.server.resource.session.close()


if __name__ == "__main__":
    unittest.main()
