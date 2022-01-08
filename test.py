import unittest
from main import get_usd_course
from main import get_btc_course
from main import get_btc_in_roubles


class TestConverter(unittest.TestCase):

    def test_usd_type(self):
        self.assertTrue(isinstance(get_usd_course(), int) or isinstance(get_usd_course(), float))

    def test_usd_value(self):
        self.assertTrue(get_usd_course() > 0)

    def test_btc_type(self):
        self.assertTrue(isinstance(get_btc_course(), int) or isinstance(get_btc_course(), float))

    def test_usd_value(self):
        self.assertTrue(get_btc_course() > 0)

    def test_rbl_type(self):
        self.assertTrue(isinstance(get_btc_in_roubles(), int) or isinstance(get_btc_in_roubles(), float))

    def test_rbl_value(self):
        self.assertTrue(get_btc_in_roubles() > 0)

if __name__ == "__main__":
    unittest.main()