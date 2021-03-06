# Stubs for requests.packages.urllib3.util.url (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Undefined, Any
from .. import exceptions

LocationParseError = exceptions.LocationParseError

url_attrs = Undefined(Any)

class Url:
    slots = Undefined(Any)
    def __new__(cls, scheme=None, auth=None, host=None, port=None, path=None, query=None, fragment=None): pass
    @property
    def hostname(self): pass
    @property
    def request_uri(self): pass
    @property
    def netloc(self): pass
    @property
    def url(self): pass

def split_first(s, delims): pass
def parse_url(url): pass
def get_host(url): pass
