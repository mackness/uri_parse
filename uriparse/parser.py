"""
    uriparse is a standards compliant module for parsing an manipulating URIs
"""

import re
import recordtype

_URI_COMPONENTS = ('scheme', 'authority', 'path', 'query', 'fragment')

class SplitResultsContainer(recordtype.recordtype('SplitResultsContainer', _URI_COMPONENTS)):
    """
        This class acts as a container for the results of the regex based URI componentization.
    """

    # RFC 3986 Appendix B
    # https://goo.gl/WVNwU3
    RE = re.compile(br"""
    (?:([^:/?#]+):)?        # scheme
    (?://([^/?#]*))?        # authority
    ([^?#]*)                # path
    (?:\?([^#]*))?          # query
    (?:\#(.*))?             # fragment
    """, flags=re.VERBOSE)

    # RFC 3986 2.2 gen-delims
    # https://goo.gl/AuU5xb
    COLON, SLASH, QUEST, HASH, LBRACKET, RBRACKET, AT = (
        u':', u'/', u'?', u'#', u'[', u']', u'@'
    )

    # RFC 3.0 Components
    # https://goo.gl/BLVqii
    SCHEME, AUTH, USER, HOST, PORT, PATH, QUERY, FRAG = (
        'scheme', 'authority', 'user', 'host', 'port', 'path', 'query', 'fragment'
    )

    EMPTY, EQL, DIGITS, AMP = '', '=',  b'0123456789', u'&'

    @property
    def userinfo(self):
        if self.authority is not None:
            userinfo, delim, _ = self.authority.rpartition(self.AT)
            if delim:
                return userinfo
            else:
                return None

    @property
    def host(self):
        authority = self.authority
        if authority is None:
            return None
        _, _, hostinfo = authority.rpartition(self.AT)
        host, _, port = hostinfo.rpartition(self.COLON)
        if port.lstrip(self.DIGITS):
            return hostinfo
        else:
            return host

    @property
    def port(self):
        authority = self.authority
        if authority is None:
            return None
        _, present, port = authority.rpartition(self.COLON)
        if present and not port.lstrip(self.DIGITS):
            return port
        else:
            return None

    def _geturi(self):
        """return full uri based on values stored in SplitResultsContainer properties"""
        scheme, authority, path, query, fragment = self
        result = []
        if scheme is not None:
            result.append(self.EMPTY.join([scheme, self.COLON]))
        if authority is not None:
            result.append(self.EMPTY.join([self.SLASH , self.SLASH, authority]))
        if path is not None:
            result.append(path)
        if query is not None:
            result.append(self.EMPTY.join([self.QUEST, query]))
        if fragment is not None:
            result.append(self.EMPTY.join([self.HASH, fragment]))
        return self.EMPTY.join(result)

    def getquery(self):
        params = {}
        if self.query:
            if self.AMP in self.query:
                for query in self.query.split(self.AMP):
                    name, _, value = query.rpartition(self.EQL)
                    params[name] = value
            else:
                name, _, value = self.query.rpartition(self.EQL)
                params[name] = value
        else:
            return None
        return params

    def appendquery(self, params):
        if params:
            if isinstance(params, dict):
                result = []
                for key, value in params.items():
                    result.append(self.EQL.join([key, value]))
                if self.query:
                    setattr(self, self.QUERY, self.AMP.join([self.query, self.AMP.join(result)]))
                else:
                    setattr(self, self.QUERY, self.AMP.join(result))
            else:
                raise TypeError('argument must be a dict')
        return self._geturi()

    def appendpath(self, path):
        if path:
            if isinstance(path, list):
                if self.path.endswith(self.SLASH):
                    setattr(self, self.PATH, self.EMPTY.join([self.path, self.SLASH.join(path)]))
                else:
                    setattr(self, self.PATH, self.SLASH.join([self.path, self.SLASH.join(path)]))
            else:
                raise TypeError('argument must be a list')
        return self._geturi()

    def update(self, attribute, value):
        if attribute not in [self.SCHEME, self.AUTH, self.PATH, self.QUERY, self.FRAG]:
             AttributeError('{} attribute is not supported'.format(attribute))

        setattr(self, attribute, value)
        return self._geturi()

def splituri(uristring):
    """
        This factory returns an instance of SplitResultsContainer that contains a 5 part tuple
        of each top level URI component as well as properties for authority sub components
        <scheme>://<authority>/<path>?<query>#<fragment>
    """
    return SplitResultsContainer(*SplitResultsContainer.RE.match(uristring).groups())

def unsplituri(parts):
    """
        This recomposes individual components back into a valid URI
        RFC 3986 5.3 https://goo.gl/kLYVDw
    """
    scheme, authority, path, query, fragment = parts
    return SplitResultsContainer(scheme, authority, path, query, fragment)._geturi()
