from enum import Enum


class ConcurrencyMode(Enum):
    NO = None
    GEVENT = 1024
    THREADING = 64
    PROCESSING = 32
