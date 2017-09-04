# uriparse

A Python module for parsing and manipulating URIs based on [RFC3986](https://tools.ietf.org/html/rfc3986)

## usage
```
from uriparse import Parser

uri = Parser('https://internet.com:8080/path?search=test#hash')
```

## run tests

`python __tests__.py -v`