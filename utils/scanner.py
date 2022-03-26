from typing import Callable, Collection, Optional

from utils.concurrency_mode import ConcurrencyMode


class Scanner:
    def __init__(self, proc: Callable, items: Collection, max_workers: Optional[int] = None,
                 mode: ConcurrencyMode = ConcurrencyMode.GEVENT):
        self.proc = proc
        self.items = items
        self.max_workers = max_workers or mode.value
        self.mode = mode
        self.bar = None

    def process_item(self, item):
        result = self.proc(item)
        self.bar()
        return result

    def execute_gevent(self):
        import gevent
        from gevent.pool import Pool as GeventPool
        pool = GeventPool(self.max_workers)
        return [i.value for i in gevent.joinall([pool.spawn(self.process_item, item) for item in self.items], 10)]

    def execute_threading(self):
        from multiprocessing.dummy import Pool as ThreadPool
        pool = ThreadPool(self.max_workers)
        return pool.map(lambda item: self.process_item(item), self.items)

    def execute_processing(self):
        from multiprocessing import Pool as ProcessPool
        pool = ProcessPool(self.max_workers)
        return pool.map(lambda item: self.process_item(item), self.items)

    def execute_serial(self):
        return map(lambda item: self.process_item(item), self.items)

    def execute(self):
        from alive_progress import alive_bar
        with alive_bar(len(self.items)) as bar:
            self.bar = bar
            return {ConcurrencyMode.NO: self.execute_serial,
                    ConcurrencyMode.GEVENT: self.execute_gevent,
                    ConcurrencyMode.THREADING: self.execute_threading,
                    ConcurrencyMode.PROCESSING: self.execute_processing}[self.mode]()
