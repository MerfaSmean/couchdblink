import json
import pathlib as pl
import random
import string
import unittest


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


class TestCaseWithCred(TestCaseBase):
    pass
