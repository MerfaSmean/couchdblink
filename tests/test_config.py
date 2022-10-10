import unittest

from couchdblink import config
from couchdblink.unittestbase import TestCaseBase


class TestConfig(TestCaseBase):
    def test_cred_url(self):
        self.assertIsInstance(config.CRED_URL, str)


if __name__ == "__main__":
    unittest.main()
