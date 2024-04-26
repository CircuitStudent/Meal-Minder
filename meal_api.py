import requests

reply = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")

if reply.status_code == 200:    # request successful
    reply_json = reply.json()   # make the reply readable
    if reply_json["meals"]:     # the reply has a key named meals
        meal = reply_json["meals"][0] # grab the meal from the list of meals
        
        # Name
        stars = "*" * (len(meal['strMeal']))
        print(stars + '\n' + meal['strMeal'] + '\n' + stars)    # name in lights

        # Ingredients
        for key, value in meal.items():         
            if 'Ingredient' in key and value:   # find ingredients
                num = ''.join(key.split('strIngredient'))   # grab index number from key
                print(meal['strMeasure' + num], value)  # show measure and ingredient

        # Instructions    
        print(stars + '\n' + meal['strInstructions'] + '\n' + stars * 3)
    else:
        print("ERROR: Did NOT find meals")
else:
    print("API ERROR")