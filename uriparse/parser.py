
"""
    uriparse is a module for parsing and
     manipulating URIs based on rfc3986
    https://goo.gl/xFd1Ab
"""

SCHEMES = ['ftp', 'http', 'gopher', 'nntp', 'telnet',
            'imap', 'wais', 'file', 'mms', 'https', 'shttp',
            'snews', 'prospero', 'rtsp', 'rtspu', 'rsync', '',
            'svn', 'svn+ssh', 'sftp','nfs','git', 'git+ssh']

class Parser(object):
    """
        Parser class is responsible for:
            - splitting a URI into it's sub components
            - inserting, deleting, updating sub components
    """
    def __init__(self, uri_param):
        self.uri = uri_param

    @property
    def scheme(self):
        """return scheme of uri"""
        scheme = self.uri.split('://')[0]
        if scheme in SCHEMES:
            return scheme

    @property
    def host(self):
        """return host of uri"""
        host = self.uri.split('://')
        if host[0] in SCHEMES:
            if host[1].split('.')[0] == 'www':
                return host[1].split('.')[1]
            else:
                return host[1].split('.')[0]
