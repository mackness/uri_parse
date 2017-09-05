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
        self.assertEqual(scheme_1, 'http', 'wrong scheme: http != ' + scheme_1)
        self.assertEqual(scheme_2, 'https', 'wrong scheme: https != ' + scheme_2)

    def test_host_property(self):
        """test the host property"""
        host_1 = Parser('http://test.com').host
        host_2 = Parser('https://internet.com').host
        self.assertEqual(host_1, 'test', 'wrong host: subdomain != ' + host_1)
        self.assertEqual(host_2, 'internet', 'wrong host: internet != ' + host_2)

if __name__ == '__main__':
    unittest.main()