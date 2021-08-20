"""
|--------------------------------------------------|
|       AUTOMATIC UPDATER FOR KALI LINUX           |
|--------------------------------------------------|
| Description   :   This script allows output      |
| Functions to developers, To minimize there work. |
|--------------------------------------------------|
| Developed By  : Paradox44                        |
| Scripted in   : Python3                          |
|--------------------------------------------------|
"""

# to clear terminal/ command prompt
import subprocess
from os import name, system

import display


def clear():
    """
    This function help  to clear your terminal/ command prompt window.
    :return: clear terminal/ command prompt window.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def update():
    try:
        subprocess.call(["sudo", "apt-get", "-y", "clean"], shell=False)
        subprocess.call(["sudo", "apt-get", "-y", "update"], shell=False)
        subprocess.call(["sudo", "apt-get", "-y", "autoremove"], shell=False)
        subprocess.call(["sudo", "apt-get", "-y", "clean"], shell=False)
    except Exception as e:
        display.error_message(True, e)


def upgrade():
    try:
        update()
        subprocess.call(["sudo", "apt-get", "-y", "upgrade"], shell=False)
        subprocess.call(["sudo", "apt-get", "-y", "full-upgrade"], shell=False)
        subprocess.call(["sudo", "apt-get", "-y", "dist-upgrade"], shell=False)
        subprocess.call(["sudo", "apt-get", "-y", "autoremove"], shell=False)
        subprocess.call(["sudo", "apt-get", "-y", "clean"], shell=False)
    except Exception as e:
        display.error_message(True, e)


def install_root():
    try:
        update()
        subprocess.call(["sudo", "apt-get", "install", "-y", "kali-root-login"], shell=False)
        print("|--------------------------------------------------|")
        print("| Root user installed successfully.                |")
        print("|--------------------------------------------------|")
        print("| Enter password for root user                     |")
        print("|--------------------------------------------------|")
        subprocess.call(["sudo", "passwd"], shell=False)
    except Exception as e:
        display.error_message(True, e)
