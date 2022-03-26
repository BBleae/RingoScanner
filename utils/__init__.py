from typing import *

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52'}


def read_items(filename: str) -> Collection[AnyStr]:
    with open(filename) as f:
        return tuple(filter(bool, map(lambda x: x.strip(), f.readlines())))
