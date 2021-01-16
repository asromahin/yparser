from sys import stdout
import threading
import queue


class Logger:
    def __init__(self, num_threads=1, urls_list=None):
        self.urls_list = urls_list
        self.num_threads = num_threads
        self.log_path = queue.Queue()
        if urls_list is not None:
            self.parsed_links = queue.Queue()
            self.counter = threading.Thread(target=self.print_progress_bar, args=[20,], daemon=True)
            self.counter.start()

    def log(self, item, thread_id=0):
        self.log_path.put({thread_id: item})

    def link_parsed(self, link=1, thread_id=0):
        self.log('-' * 60, thread_id)
        if self.urls_list is not None:
            self.parsed_links.put(link)

    def itemize_logs(self):
        log_dict = {}
        while not self.log_path.empty():
            item = self.log_path.get()
            self.log_path.task_done()
            key = int(str(item.keys()).replace('dict_keys([', '').replace('])', ''))
            value = [str(item.values()).replace('dict_values([', '').replace('])', '')]
            if key in log_dict.keys():
                log_dict[key] += value
            else:
                log_dict[key] = value
        return log_dict

    @staticmethod
    def print_logs_to_console(log_dict):
        for k, v in log_dict.items():
            print('*' * 60)
            print(f'Thread {k}')
            print('*' * 60)
            for record in v:
                if record.isdigit():
                    print(record)
                else:
                    print(record[1:-1])
            print('')

    @staticmethod
    def write_logs_to_txt(log_dict):
        print('Writing to txt...')
        with open('log.txt', 'w') as file:
            for k, v in log_dict.items():
                file.write('*' * 60 + '\n')
                file.write(f'Thread {k}' + '\n')
                file.write('*' * 60 + '\n')
                for record in v:
                    if record.isdigit():
                        file.write(record + '\n')
                    else:
                        file.write(record[1:-1] + '\n')
                file.write('' + '\n')
        print('Written to txt')

    def end_logging(self, log_to_txt=False, log_to_console=True):
        log_dict = self.itemize_logs()
        if self.urls_list is not None:
            self.parsed_links.join()
        if log_to_console:
            self.print_logs_to_console(log_dict)
        if log_to_txt:
            self.write_logs_to_txt(log_dict)

    def print_progress_bar(self, bar_length):
        counter = 0
        while True:
            if counter != len(self.urls_list):
                stdout.write(
                    '\r{}{}| {:.0f}% | {}/{} links parsed'.format('█' * counter * (bar_length // len(self.urls_list)),
                                                                  '-' * (len(self.urls_list) - counter) * (
                                                                          bar_length // len(self.urls_list)),
                                                                  counter / len(self.urls_list) * 100,
                                                                  counter,
                                                                  len(self.urls_list)))
            else:
                stdout.write(
                    '\r{}{}| {:.0f}% | {}/{} links parsed\n\n'.format(
                        '█' * counter * (bar_length // len(self.urls_list)),
                        '-' * (len(self.urls_list) - counter) * (
                                bar_length // len(self.urls_list)),
                        counter / len(self.urls_list) * 100,
                        counter,
                        len(self.urls_list)))
            url = self.parsed_links.get()
            counter += 1
            self.parsed_links.task_done()
