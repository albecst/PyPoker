import os
def clear_console():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Unix (Linux y macOS)
    else:
        os.system('clear')