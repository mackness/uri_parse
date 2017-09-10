"""uriparse test file"""

import unittest
from uriparse import splituri, unsplituri

class Tests(unittest.TestCase):
    """uriparse test class"""

    def test_properties(self):
        """test SplitResultsContainer class memebers"""
        uri = 'foo://username:password@www.example.com:123/hello/world/there.html?name=ferret#foo'
        self.assertEquals(splituri(uri).scheme, 'foo')
        self.assertEquals(splituri(uri).authority, 'username:password@www.example.com:123')
        self.assertEquals(splituri(uri).path, '/hello/world/there.html')
        self.assertEquals(splituri(uri).fragment, 'foo')
        self.assertEquals(splituri(uri).userinfo, 'username:password')
        self.assertEquals(splituri(uri).host, 'www.example.com')
        self.assertEquals(splituri(uri).port, '123')

    def test_split_factory(self):
        """test splituri and unsplituri factory functions"""
        cases = [
            ('foo://example.com:8042/over/there?name=ferret#nose',
             ('foo', 'example.com:8042', '/over/there', 'name=ferret', 'nose')),
            ('file:///Users/macksol/Desktop/Book.html',
             ('file', '', '/Users/macksol/Desktop/Book.html', None, None)),
            ('arn:aws:elasticbeanstalk:us-east-1',
             ('arn', None, 'aws:elasticbeanstalk:us-east-1', None, None)),
        ]

        for uri, parts in cases:
            self.assertEquals(tuple(splituri(uri)), parts)

    def test_unsplit_factory(self):
        """test splituri and unsplituri factory functions"""
        cases = [
            (('foo', 'example.com:8042', '/over/there', 'name=ferret', 'nose'),
             'foo://example.com:8042/over/there?name=ferret#nose'),
            (('file', '', '/Users/macksol/Desktop/Book.html', None, None),
             'file:///Users/macksol/Desktop/Book.html'),
            (('arn', None, 'aws:elasticbeanstalk:us-east-1', None, None),
             'arn:aws:elasticbeanstalk:us-east-1'),
        ]

        for uri, parts in cases:
            self.assertEquals(unsplituri(uri), parts)

    def test_split_uri(self):
        """test split uri method"""
        cases = [
            ('foo://username:password@www.example.com:123&?name=ferret&id=123',
             {'name': 'ferret', 'id': '123'}),
            ('https://www.google.com/search?q=42&oq=42&&sourceid=chrome&ie=UTF-8',
             {'q': '42', '': '', 'sourceid': 'chrome', 'ie': 'UTF-8', 'oq': '42'}),
            ('https://www.google.com/search?q=42&oq=42&&sourceid=chrome&ie=UTF-8#frag',
             {'q': '42', '': '', 'sourceid': 'chrome', 'ie': 'UTF-8', 'oq': '42'})
        ]

        for uri, dictionary in cases:
            self.assertEquals(splituri(uri).getquery(), dictionary)

    def test_appendquery(self):
        """test appending query parameters"""
        cases = [
            ({'id':'123'},
             'https://goo.gl/GjxaRz',
             'https://goo.gl/GjxaRz?id=123'),
            ({'id':'123', 'user':'mack', 'xid':'d4d874a8d34040b0c29e0dd526d0b20a75448e44'},
             'foo://username:password@www.example.com:123?name=ferret',
             'foo://username:password@www.example.com:123?name=ferret&xid=d4d874a8d34040b0c29e0dd526d0b20a75448e44&id=123&user=mack'),
            ({'id':'123'},
             'foo://username:password@www.example.com:123?name=ferret#hash',
             'foo://username:password@www.example.com:123?name=ferret&id=123#hash')
        ]

        for param, uri, result in cases:
            self.assertEquals(splituri(uri).appendquery(param), result)

    def test_appendpath(self):
        """test appending path components"""
        cases = [
            (['path'],
             'https://goo.gl/GjxaRz/',
             'https://goo.gl/GjxaRz/path'),
            (['deep','deep','123','path'],
             'https://goo.gl/#hash',
             'https://goo.gl/deep/deep/123/path#hash'),
        ]

        for param, uri, result in cases:
            self.assertEquals(splituri(uri).appendpath(param), result)

    def test_update(self):
        """test updating URI components"""
        cases = [
            (('scheme','http'),
             'https://goo.gl/GjxaRz/',
             'http://goo.gl/GjxaRz/'),
            (('fragment','div'),
             'foo://example.com:8042/over/there?name=ferret#nose',
             'foo://example.com:8042/over/there?name=ferret#div'),
            (('authority','reddit.com:8080'),
             'foo://example.com:8042/over/there?name=ferret#nose',
             'foo://reddit.com:8080/over/there?name=ferret#nose'),
            (('scheme','http'),
             'foo://example.com:8042/over/there?name=ferret#nose',
             'http://example.com:8042/over/there?name=ferret#nose'),
            (('path','/over/where'),
             'http://example.com:8042/over/there?name=ferret#nose',
             'http://example.com:8042/over/where?name=ferret#nose')
        ]

        for params, uri, result in cases:
            self.assertEquals(splituri(uri).update(params[0], params[1]), result)

if __name__ == '__main__':
    unittest.main()
