from sys import stdout


def print_log_to_console(log_path, num_threads):
    for i in range(num_threads):
        record = log_path.get()
        print('*' * 60)
        print(f'Record {i + 1}')
        print('*' * 60)
        for row in record:
            if '[[' not in str(row):
                print(str(row).replace('[', '').replace(']', '').replace("',", '').replace("'", ''))
            else:
                if str(row) == '[[]]':
                    print('No errors to log')
                else:
                    row = str(row).split(sep='], [')
                    for item in row:
                        print(item.replace('[[[', '').replace(']]]', ''))
        print('')


def print_progress_bar(parsed_links, image_urls, bar_length):
    counter = 0
    while True:
        if counter != len(image_urls):
            stdout.write('\r{}{}| {:.0f}% | {}/{} links parsed'.format('█' * counter * (bar_length // len(image_urls)),
                                                                       '-' * (len(image_urls) - counter) * (
                                                                                   bar_length // len(image_urls)),
                                                                       counter / len(image_urls) * 100,
                                                                       counter,
                                                                       len(image_urls)))
        else:
            stdout.write(
                '\r{}{}| {:.0f}% | {}/{} links parsed\n\n'.format('█' * counter * (bar_length // len(image_urls)),
                                                                '-' * (len(image_urls) - counter) * (
                                                                        bar_length // len(image_urls)),
                                                                counter / len(image_urls) * 100,
                                                                counter,
                                                                len(image_urls)))
        url = parsed_links.get()
        counter += 1
        parsed_links.task_done()


def write_log_to_txt(log_path, filename, num_threads):
    with open(f'{filename}.txt', 'w') as file:
        for i in range(num_threads):
            record = log_path.get()
            file.write('*' * 60 + '\n')
            file.write(f'Record {i + 1}' + '\n')
            file.write('*' * 60 + '\n')
            for row in record:
                if '[[' not in str(row):
                    file.write(str(row).replace('[', '').replace(']', '').replace("',", '').replace("'", '') + '\n')
                else:
                    if str(row) == '[[]]':
                        file.write('No errors to log' + '\n')
                    else:
                        row = str(row).split(sep='], [')
                        for item in row:
                            file.write(item.replace('[[[', '').replace(']]]', '') + '\n')
            file.write('\n')
