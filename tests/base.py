import json
import pathlib as pl
import random
import string
import unittest

import couchdblink.server_functions as sfn


class TestCaseBase(unittest.TestCase):
    @staticmethod
    def assertIsFile(path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    @staticmethod
    def assertFileIsJSON(path):
        try:
            with open(path) as f:
                json.load(f)
        except json.decoder.JSONDecodeError:
            raise AssertionError("File does not decode as JSON: %s" % str(path))

    @staticmethod
    def random_str(k=21, prefix=""):
        return prefix + "".join(
            random.choices(string.ascii_lowercase + string.digits, k=k)
        )


class TestCaseWithDb(TestCaseBase):
    cred_url = None
    delete_db_in_tearDown = True

    def setUp(self):
        self.server = sfn.get_couchdb_connection(self.cred_url)
        self.test_name = self.random_str(16, prefix="test")
        self.server.create(self.test_name)

    def tearDown(self):
        if self.delete_db_in_tearDown:
            self.server.delete(self.test_name)
        self.server.resource.session.close()
