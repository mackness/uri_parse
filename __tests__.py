"""uriparse test file"""

import unittest
from uriparse import Parser

class Test(unittest.TestCase):
    """uriparse test file"""

    def parser_initialization_test(self):
        """test parser initialization"""
        self.assertIsNotNone(Parser('https://test.com'))

if __name__ == '__main__':
    unittest.main()
