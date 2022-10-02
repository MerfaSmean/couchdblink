import unittest
import json
import pathlib as pl


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
