# Stubs for xml.etree.ElementInclude (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Undefined, Any

XINCLUDE = Undefined(Any)
XINCLUDE_INCLUDE = Undefined(Any)
XINCLUDE_FALLBACK = Undefined(Any)

class FatalIncludeError(SyntaxError): pass

def default_loader(href, parse, encoding=None): pass
def include(elem, loader=None): pass
