import unittest

from pycouchdb import client
from requests.exceptions import ConnectionError

import couchdblink.server_functions as sfn
import local_config
from couchdblink.unittestbase import TestCaseBase, TestCaseWithDb


class TestGetCouchdbConnection(TestCaseBase):
    def test_connection_no_args(self):
        s = sfn.get_couchdb_connection()
        self.assertIn("version", s.info())
        sfn.close(s)

    def test_connection_lan_server(self):
        s = sfn.get_couchdb_connection(local_config.lan_server_url)
        self.assertIn("version", s.info())
        sfn.close(s)

    def test_connection_lan_server_fail(self):
        s = sfn.get_couchdb_connection(local_config.lan_server_url_wrong)
        try:
            s.info()
        except ConnectionError:
            pass
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
    cred_url = local_config.lan_server_cred_url

    def test_get_db(self):
        db = sfn.get_make_db(self.server, self.test_name)
        self.assertIsInstance(db, client.Database)


if __name__ == "__main__":
    unittest.main()
