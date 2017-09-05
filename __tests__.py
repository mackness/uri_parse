"""uriparse test file"""

import unittest
from uriparse import Parser, is_int

class Tests(unittest.TestCase):
    """uriparse test file"""

    def parser_initialization_test(self):
        """test parser initialization"""
        self.assertIsNotNone(Parser('https://test.com'))

    """
        utility tests
    """

    def test_is_int_util(self):
        """test the is_int utility"""
        self.assertTrue(is_int(1))
        self.assertFalse(is_int('a66378795e0b23491b9fb1c2c4b29ca8cfc7bf8c'))

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

    def test_port_property(self):
        """test the port property"""
        port_1 = Parser('http://internet.com:8080/xpath/ypath/zpath#hash').port
        port_2 = Parser('http://internet.com:3000/another/path').port
        self.assertEqual(port_1, '8080', 'wrong port: 8080 != ' + port_1)
        self.assertEqual(port_2, '3000', 'wrong port: 3000 != ' + port_2)

    def test_path_property(self):
        """test the path property"""
        path_1 = Parser('http://internet.com:8080/xpath/ypath/zpath').pathname
        path_2 = Parser('https://reddit.com/r/python').pathname
        self.assertEqual(path_1, '/xpath/ypath/zpath', 'wrong path: /xpath/ypath/zpath != ' + path_1)
        self.assertEqual(path_2, '/r/python', 'wrong path: /r/python != ' + path_2)

    def test_params_property(self):
        """test params property"""
        params_1 = Parser('http://reddit.com:8080/r/python?user=mack#frag').params
        params_2 = Parser('http://reddit.com:8080/r/python?user=mack&id=123').params
        self.assertEqual(params_1, 'user=mack', 'wrong params: user=mack  != ' + params_1)
        self.assertEqual(params_2, 'user=mack&id=123', 'wrong params: user=mack&id=123  != ' + params_2)

if __name__ == '__main__':
    unittest.main()
