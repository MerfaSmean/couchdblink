import unittest
import json
import pathlib as pl

from couchdblink.nogit import extra_config


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


class TestNoGitExtraConf(TestCaseBase):
    def test_cred_json_file_path(self):
        self.assertIsInstance(extra_config.DEFAULT_CRED_JSON_FILE_PATH, str)

    def test_cred_json_file(self):
        self.assertIsFile(extra_config.DEFAULT_CRED_JSON_FILE_PATH)

    def test_cred_json(self):
        self.assertFileIsJSON(extra_config.DEFAULT_CRED_JSON_FILE_PATH)

    def test_cred_url(self):
        path = extra_config.DEFAULT_CRED_JSON_FILE_PATH
        fail_msg = "'url' not found in data loaded from file: %s"
        with open(path) as f:
            data = json.load(f)
        if "url" not in data:
            raise AssertionError(fail_msg % str(path))


if __name__ == "__main__":
    unittest.main()
