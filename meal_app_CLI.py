import os
import time
import requests

size = os.get_terminal_size()

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def title_banner():
    title = "Meal Minder"
    tab = (size.columns - (len(title) + 2)) // 2
    print(size.columns * '~')
    print(tab * '/' + title + tab * '\\')
    print(size.columns * '~')

def menu_banner(title):
    tab = (size.columns - (len(title) + 2)) // 2    
    print(tab * '<' + title + tab * '>')
    print(size.columns * '~')

def main_display():
    menu_banner("Main Menu")
    menu_string = """
1) Random Meal
2) Choice 2
Q for QUIT
"""
    menu_list = menu_string.split('\n')
    tab = (size.columns - max([len(line) for line in menu_list])) // 2
    for line in menu_list:
        print(tab * ' ' + line)

def random_meal():
    menu_banner("Random Meal")
    reply = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")

    if reply.status_code == 200:    # request successful
        reply_json = reply.json()   # make the reply readable
        if reply_json["meals"]:     # the reply has a key named meals
            meal = reply_json["meals"][0] # grab the meal from the list of meals

            # Name
            stars = "-" * (len(meal['strMeal']))
            print(meal['strMeal'] + '\n' + stars)    # name in lights

            # Ingredients
            for key, value in meal.items():         
                if 'Ingredient' in key and value:   # find ingredients
                    num = ''.join(key.split('strIngredient'))   # grab index number from key
                    print(meal['strMeasure' + num], value)  # show measure and ingredient

            # Instructions    
            spacer = size.columns * '*'
            print(spacer + '\n' + meal['strInstructions'] + '\n' + spacer)
        else:
            print("ERROR: Did NOT find meals")
    else:
        print("API ERROR")

def main_menu():
    while True:
        clearscreen()
        title_banner()
        main_display()
        select_string = "Select an option: "
        tab = (size.columns - len(select_string)) // 2
        selection = input(tab * ' ' + select_string)
        match selection:
            case '1':
                clearscreen()
                title_banner()
                random_meal()
                print()
                input("Press ENTER to return to Main Menu")
            case '2':
                clearscreen()
                title_banner()
                menu_banner("Choice 2")
                time.sleep(2)
            case 'Q' | 'q': 
                print()
                print(tab * ' ' + "Program Complete")
                print()
                return
            case _:
                print()
                redo_string = "Please choose from the given options."
                tab = (size.columns - len(redo_string)) // 2
                print(tab * ' ' + redo_string)
                time.sleep(3)
    
if __name__ == '__main__':
    main_menu()