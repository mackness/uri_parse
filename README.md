# uriparse

A Python module for parsing and manipulating URIs based on [RFC3986](https://tools.ietf.org/html/rfc3986)

## usage
```
from uriparse import Parser

uri = Parser('https://internet.com:8080/path?search=test#hash')
```

## properties

uri.scheme\
uri.subdomain\
uri.host\
uri.port\
uri.pathname\
uri.params\
uri.fragment

## methods

uri.set_scheme()\
uri.delete_scheme()\
uri.set_host()\
uri.set_port()\
uri.delete_port()\
uri.set_params()\
uri.delete_params()\
uri.set_pathname()\
uri.delete_pathname()\
uri.set_pathname()\
uri.delete_pathname()

## run tests

`python __tests__.py -v`

## feature wishlist / code improvements
- URI validation
- URI normalization
- URL, URI, URN identification
- comprehensive mailto: url support
- better warning / error handling
- more robust and diverse test cases
- URI templating or method chaining