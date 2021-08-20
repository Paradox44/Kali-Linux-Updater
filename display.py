"""
|--------------------------------------------------|
|       AUTOMATIC UPDATER FOR KALI LINUX           |
|--------------------------------------------------|
| Description   :   This script allows output      |
| Functions to developers, To minimize there work. |
|--------------------------------------------------|
| Developed By  : Athena                           |
| Scripted in   : Python3                          |
|--------------------------------------------------|
"""
import sys


def welcome_message():
    """
    This function is use to display the welcome message to the user.
    :return:
    """
    print("|--------------------------------------------------|")
    print("|          AUTOMATIC KALI LINUX UPDATER            |")
    print("|--------------------------------------------------|")
    print("| Version    :   0.0.0.1                           |")
    print("| Build      :   BETA-B-03082021P0807_KALI-LINUX   |")
    print("|--------------------------------------------------|")
    print("|                TEAM ALCHEMISTS                   |")
    print("|--------------------------------------------------|")
    print("| Developed  :     Github      |       Twitter     |")
    print("| Menu       :     Itachi-91   |      itachi_9197  |")
    print("| Algorithms :     Paradox44   |      Paradox_044  |")
    print("| UI/ UX     :     Athena_077  |      Athena_077   |")
    print("|--------------------------------------------------|")
    return True


def good_bye_message():
    """
    To display exit message to user.
    :return:
    """
    welcome_message()
    print("| We hope you like our work. If yes the comment us |")
    print("| Github or Twitter. Thank You.                    |")
    print("|--------------------------------------------------|")
    return True


def error_message(fatal_error, message):
    """
    This function is created to display error message in proper manner.
    :param fatal_error: is boolean, use for terminate program if fatal error is occurred.
    :param message: message want to display, we use this for exception techniques.
    :return: display error message in proper manner.
    """
    try:
        print("|--------------------------------------------------|")
        print("| ERROR #1 : SOMETHING WRONG HERE.                 |")
        print("|--------------------------------------------------|")
        print("|                ERROR MESSAGE                     |")
        print("|--------------------------------------------------|")
        print(str(message))
        print("|--------------------------------------------------|")
        if fatal_error:
            sys.exit()
        return True
    except Exception as e:
        print("|--------------------------------------------------|")
        print("| ERROR #2 : SOMETHING WRONG HERE.                 |")
        print("|--------------------------------------------------|")
        print("|                    ERROR MESSAGE                 |")
        print("|--------------------------------------------------|")
        print(str(e))
        print("|--------------------------------------------------|")
        sys.exit()