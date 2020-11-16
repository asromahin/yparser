import os
import signal
import wmi
import psutil


def kill_chrome_instances():
    """
    Killing instances of Google Chrome created by YandexParser
    """
    # Initializing the wmi constructor
    f = wmi.WMI()

    # Printing the header for the later columns
    print('\nKilling Google Chrome instances...')

    # # Iterating through all the running processes
    # for process in f.Win32_Process():
    #     # Displaying the P_ID and P_Name of the process
    #     # print(f"{process.ProcessId:<10} {process.Name}")
    #     if 'chrome' in process.Name:
    #         os.kill(process.ProcessId, signal.SIGTERM)

    k = 0
    for process in psutil.process_iter():
        if 'chrome' in process.name():
            process.kill()
            k += 1

    print(f'{k} processes killed')

