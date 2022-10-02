import unittest

from base import TestCaseBase
from couchdblink import config


class TestConfig(TestCaseBase):
    def test_cred_url(self):
        self.assertIsInstance(config.CRED_URL, str)


if __name__ == '__main__':
    unittest.main()
