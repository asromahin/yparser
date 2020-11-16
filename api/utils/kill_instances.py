import os
import signal
import wmi
import time


def kill_chrome_instances():
    """
    Killing instances of Google Chrome created by YandexParser
    """
    # Initializing the wmi constructor
    f = wmi.WMI()

    # Printing the header for the later columns
    print('\nKilling Google Chrome instances...')

    # Iterating through all the running processes
    for process in f.Win32_Process():
        # Displaying the P_ID and P_Name of the process
        # print(f"{process.ProcessId:<10} {process.Name}")
        if 'chrome' in process.Name:
            # First trying to send SIGTERM and SIGSTOP and then again sending SIGSTOP
            # Have no f*cking clue how this works, but it does, so... deal with it)
            try:
                os.kill(process.ProcessId, signal.SIGTERM)
            except PermissionError:
                continue

            try:
                os.kill(process.ProcessId, signal.SIGSTOP)
            except AttributeError:
                continue

            os.kill(process.ProcessId, signal.SIGSTOP)
