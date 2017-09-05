"""
    uriparse is a module for parsing and
     manipulating URIs based on rfc3986
    https://goo.gl/xFd1Ab
"""

import re
from .utils import is_int

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

    @property
    def port(self):
        """return port of uri"""
        port = self.uri.split(':')

        if is_int(port[-1]):
            return port[-1]
        else:
            for part in port[-1].split('/'):
                if is_int(part):
                    return part

    @property
    def pathname(self):
        """return pathname of uri"""
        result = []
        for part in self.uri.split('/'):
            if re.match("^[a-zA-Z0-9_]*$", part):
                result.append(part)
        return '/'.join(result)

    @property
    def params(self):
        """return params of uri"""
        params = self.uri.split('?')[-1]
        if '#' in params:
            return params.split('#')[0]
        else:
            return params

    @property
    def fragment(self):
        """return fragment of uri"""
        return self.uri.split('#')[-1]

    def set_scheme(self, scheme):
        """return full uri with updated scheme"""
        if self.scheme:
            return self.uri.replace(self.scheme, scheme)
        else:
            return scheme + '://' + self.uri

    def delete_scheme(self):
        """delete scheme and return remaining uri"""
        return self.set_scheme('').split('://')[-1]