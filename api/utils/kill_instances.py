import psutil


def get_all_children(proc):
    res = []
    res += proc.children()
    for child in proc.children():
        res += get_all_children(child)
    return res


def kill_chrome_instances():
    """
    Killing instances of Google Chrome created by YandexParser
    """
<<<<<<< HEAD

    print('\nKilling Google Chrome instances...')

=======
    print('\nKilling Google Chrome instances...')
>>>>>>> 236cf2f7ab14131b31b9f853512bb74a3118e4ac
    found = 0
    killed = 0
    kill_chromium = 0
    for process in psutil.process_iter():
        if 'chrome' in process.name():
<<<<<<< HEAD
            if process.name() == 'chromedriver.exe':
                childrens = get_all_children(process)
                for child in childrens:
                    child.terminate()
                    killed += 1
                process.terminate()
                killed += 1
                kill_chromium += 1
=======
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
>>>>>>> 236cf2f7ab14131b31b9f853512bb74a3118e4ac
            found += 1

    print(f'\n{found} processes found')
    print(f'{killed} processes killed')


if __name__ == "__main__":
    kill_chrome_instances()