
"""
    uriparse is a module for parsing and
     manipulating URIs based on rfc3986
    https://goo.gl/xFd1Ab
"""

class Parser(object):
    """
        Parser class is responsible for:
            - splitting a URI into it's sub components
            - inserting, deleting, updating sub components
    """
    def __init__(self, uri_param):
        self.uri = uri_param
