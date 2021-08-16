"""
|--------------------------------------------------|
|       AUTOMATIC UPDATER FOR KALI LINUX           |
|--------------------------------------------------|
| Description   :   This script allows output      |
| Functions to developers, To minimize there work. |
|--------------------------------------------------|
| Developed By  : Itachi-91                        |
| Scripted in   : Python3                          |
|--------------------------------------------------|
"""
import display
import functions

def menu():
    try:
        display.welcome_message()
        print("|              AVAILABLE OPTIONS                   |")
        print("|--------------------------------------------------|")
        print("|    1   |   UPDATE  KALI LINUX                    |")
        print("|    2   |   UPGRADE KALI LINUX                    |")
        print("|    3   |   INSTALL ROOT USER FOR KALI LINUX      |")
        print("|    0   |   EXIT & CLOSE THIS SCRIPT              |")
        print("|--------------------------------------------------|")
        menu_input = int(input("|   ENTER YOUR CHOICE   :                       "))
        if menu_input == 1:
            display.welcome_message()
            functions.clear()
            print("| UPDATEATING  KALI LINUX                          |")
            print("|--------------------------------------------------|")
            functions.update()
        elif menu_input == 2:
            display.welcome_message()
            functions.clear()
            print("| UPGRADING  KALI LINUX                            |")
            print("|--------------------------------------------------|")
            functions.upgrade()
        elif menu_input == 3:
            display.welcome_message()
            functions.clear()
            print("| INSTALLING ROOT_LOGIN IN  KALI LINUX             |")
            print("|--------------------------------------------------|")
            function.install_root()
        else:
            display.good_bye_message()
    except Exception as e:
        display.error_message(False, e)


menu()