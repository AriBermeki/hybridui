from importlib_metadata import version
from pathlib import Path

project_root = Path(__file__).parent

__version__ = version(__package__)


from . import elements, globals, interface

APP = 'globals:app'
__all__ = [

    'elements',
    'globals',
    'interface',
    'hybrid',
    'client',
    '__version__',
]