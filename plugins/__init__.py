import glob
import os.path
from gevent import monkey
monkey.patch_all()

_modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
__all__ = [os.path.basename(_f)[:-3] for _f in _modules if os.path.isfile(_f) and not _f.endswith('__init__.py')]


def get_plugins():
    return __all__


def get_plugin(selected_plugin):
    return __import__(__name__ + "." + selected_plugin, fromlist=__all__)
