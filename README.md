# uriparse

A standards compliant Python module for parsing and manipulating URIs [RFC3986](https://tools.ietf.org/html/rfc3986)

## Usage
```
from uriparse import splituri, unsplituri

# splituri
>>> uri = 'https://john:doe@internet.com:8080/path?search=test#hash'
>>> splituri(uri)
SplitResultContainer(scheme='https', authority='internet.com:8080', path='/path', query='search=test', fragment='hash')

>>> splituri(uri).scheme
'https'

>>> splituri(uri).authority
'internet.com:8080'

>>> splituri(uri).userinfo
'john:doe'

...

# splituri is a factory function that returns an instance
# of SplitResultsContainer which contains a 5 item tuple of the split
# results all of the  properties and methods documented below

# unsplituri()
>>> unsplituri(('http', 'internet.com:8080', 'path', 'id=123', 'hash'))
'http://internet.com:8080path?id=123#hash'

# unsplit uri will take all of 5 top level parts of a URI as a tuple and
# compose them back together to for a complete and valid URI

...

# getquery()
# should be noted that it's possible to use getquery to access individual params.
>>> uri = 'https://john:doe@internet.com:8080/path?search=test&id=123#hash'
>>> splituri(uri).getquery().get('search')
'test'

...

# update()
>>> uri = 'https://john:doe@internet.com:8080/path?search=test&id=123#hash'
>>> splituri(uri).update('scheme', 'http')
'http://john:doe@internet.com:8080/path?search=test&id=123#hash'

# update can also be used to remove URI parts
>>> uri = 'https://john:doe@internet.com:8080/path?search=test&id=123#hash'
>>> splituri(uri).update('hash', '')
'http://john:doe@internet.com:8080/path?search=test&id=123'

# the supported parts for this operation are scheme, authority, path, query, and fragment

```

## Attributes
.`scheme`\
.`authority`\
.`userinfo`\
.`host`\
.`port`\
.`path`\
.`query`\
.`fragment`

## Methods
- getquery()
    * `description` Get all the query parameters as a dict.
    * `arguments` None
    * `return` a dict of all the query params in the URI

- appendquery({key:string, value:string}:dict)
    * `description` If query params exist this method will append to them, if they do not exist this method will set them.
    * `arguments` takes one dict argument
    * `return` full URI

- appendpath([value:string, value:string]:list)
    * `description` Tf path exists this method will append to it, if it does not exist this method will set it.
    * `arguments` takes 1 list argrument
    * `return` full URI

- update(attribute:string, value:string)
    * `description` This is a generic update method. It will replace the specified attribute with the supplied value. All top level URI components are supported. Authority sub components are not supported at this time. If an invalid attribute is passed, update will throw a AttributeError. Note, update does not care if the value exists or not. In other words even if you pass a value for a part that does not exist the part will be set with the passed value.
    * `arguments` takes two string arguments
    * `return` full URI

## Run Tests

`python __tests__.py -v`

## Feature Wishlist
- URL URN identificaiton
- Currently errors are handled in SplitResultsContainer but creating an error handling subclass my be a nice separation of concerns
- method chaining and URI templating

## Limitations
- this module does not fully support IP based host formats [7.4](https://tools.ietf.org/html/rfc3986#section-7.4)

## Contributing
- Best way to extend this module:
    - add method to SplitResultsContainer class in uriparse/split.py
    - add unit test to ./__tests__.py
    - write documentation for method in __methods__ section

