import os

from yparser.src.pool import Pool, PoolInstance


class Hasher(PoolInstance):
    def __init__(self, input_queue, output_queue=None, logger_queue=None):
        """Инициализация потока"""
        super(Hasher, self).__init__(input_queue, output_queue, logger_queue)

    def run_func(self, path):
        pass


class HasherPool(Pool):
    def __init__(self, n_workers, output_queue=None):
        super(HasherPool, self).__init__(
            pool_instance=Hasher,
            n_workers=n_workers,
            output_queue=output_queue,
        )


class HashResult:
    def __init__(self, path: str, hash):
        self.path = path
        self.hash = hash