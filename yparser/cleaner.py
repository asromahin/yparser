from yparser.src.cleaner.hasher import HasherPool


class Cleaner:
    def __init__(self, n_workers=1):
        self.hasher_pool = HasherPool(n_workers=n_workers)
