

#from ._version import get_versions
#__version__ = get_versions()['version']
#version = __version__
#del get_versions

from .datastructures import *
from .database import *


from . import _version
__version__ = _version.get_versions()['version']
