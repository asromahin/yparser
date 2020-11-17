import psutil


def kill_chrome_instances():
    """
    Killing instances of Google Chrome created by YandexParser
    """
    print('\nKilling Google Chrome instances...')
    found = 0
    killed = 0
    for process in psutil.process_iter():
        if 'chrome' in process.name():
            parents_list = [item.name() for item in process.parents()]
            print(' | '.join([f'\nPID: {process.pid}',
                              f'Process name: {process.name()}',
                              f'Parent\'s names: {parents_list}',
                              f'{process.children()}'
                              ]), end='\t')
            if 'explorer.exe' not in parents_list:
                print('- to kill', end='')
                process.terminate()
                killed += 1
            found += 1

    print(f'\n{found} processes found')
    print(f'{killed} processes killed')
