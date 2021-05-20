import threading
from queue import Queue
import uuid


class PoolInstance(threading.Thread):
    def __init__(self, input_queue, output_queue=None, logger_queue=None):
        """Инициализация потока"""
        threading.Thread.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.logger_queue = logger_queue
        self.id = str(uuid.uuid4())

    def run(self):
        while True:
            data = self.input_queue.get()
            out_data = self.run_func(data)
            if out_data is not None and self.output_queue is not None:
                self.output_queue.put(out_data)
            self.input_queue.task_done()

    def run_func(self, data):
        return None


class Pool:
    def __init__(self, n_workers, pool_instance, *args, output_queue=None, logger_queue=None, **kwargs):
        self.n_workers = n_workers
        self.input_queue = Queue()
        self.output_queue = output_queue
        self.logger_queue = logger_queue
        for i in range(n_workers):
            t = pool_instance(input_queue=self.input_queue, output_queue=self.output_queue, logger_queue=logger_queue, *args, **kwargs)
            t.setDaemon(True)
            t.start()
