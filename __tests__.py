"""uriparse test file"""

import unittest
from uriparse import Parser

class Test(unittest.TestCase):
    """uriparse test file"""

    def parser_initialization_test(self):
        """test parser initialization"""
        self.assertIsNotNone(Parser('https://test.com'))

    """
        property tests
    """

    def test_scheme_property(self):
        """test the scheme property"""
        scheme_1 = Parser('http://test.com').scheme
        scheme_2 = Parser('https://test.com').scheme
        self.assertEqual(scheme_1, 'http', 'did not retrieve correct scheme')
        self.assertEqual(scheme_2, 'https', 'did not retrieve correct scheme')

if __name__ == '__main__':
    unittest.main()
