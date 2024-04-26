import os
import time

size = os.get_terminal_size()

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_banner():  
    title = "Main Menu"
    tab = (size.columns - (len(title) + 2)) // 2
    print(size.columns * '*')
    print(f"{tab * '*'} {title} {tab * '*'}")
    print(size.columns * '*')

def main_display():
    clearscreen()
    main_banner()
    menu_string = """
1) Choice 1
2) Choice 2
Q for QUIT
"""
    menu_list = menu_string.split('\n')
    tab = (size.columns - max([len(line) for line in menu_list])) // 2
    for line in menu_list:
        print(tab * ' ' + line)

def main_menu():
    while True:
        main_display()
        select_string = "Select an option: "
        tab = (size.columns - len(select_string)) // 2
        selection = input(tab * ' ' + select_string)
        match selection:
            case '1':
                clearscreen()
                print("Choice 1\n")
                time.sleep(2)
            case '2':
                clearscreen()
                print("Choice 2\n")
                time.sleep(2)
            case 'Q' | 'q': 
                clearscreen()
                print("Program Complete")
                print()
                return
            case _:
                print()
                print("Please choose from the given options.")
                time.sleep(3)
    
if __name__ == '__main__':
    main_menu()
    
