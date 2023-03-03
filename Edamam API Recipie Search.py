import requests

app_id = "02198055"
app_key = "5e10e0c9729fd05484f79217ef8bb16d"


cuisine = ["British", "Italian", "Mexican", "Indian", "Chinese"] # cuiine selection options
diet = ["Vegetarian", "Vegan", "Alcohol-free", "Gluten-free"] # diet selection options

# defines variables to be used for including API parameters
includeAppId = "app_id={}".format(app_id)
includeAppKey = "app_key={}".format(app_key)
includecuisine = ""
includediet = ""

# prompt to ask user to enter ingredients

ingredient = input("Enter ingredients: ")
while ingredient == "":
    ingredient = input("You must enter at least one ingredient. Try again: ")
# use split and join functions to enable selection of more than one ingredient
components = ingredient.split()
items = ",+".join(components) or "and+".join(components) or " +".join(components)
ingredients = "ingredients=" + items
includeIngredients = "q={}".format(ingredients)

# prompt to ask user to enter cuisine preference (if any)
cuisine_choice = input(
    f"What cuisine would you like?\n{cuisine}: ")
while (cuisine_choice != "") and (cuisine_choice not in cuisine):
    cuisine_choice = input(
        f"Invalid response. Choose your preferred cuisine from the following, or press enter if none\n{cuisine}: ")
    cuisine_flag = 0
if cuisine_choice == "" :
    cuisine_flag = 0
elif cuisine_choice in cuisine:
    includecuisine = f'Cuisine={cuisine_choice}'
    cuisine_flag = 1



# asks user to enter dietary requirements (if any)
diet_choice = input(
    f"What diet would you like? \n{diet}: ")
while (diet_choice != "") and (diet_choice not in diet):
    diet_choice = input(
        f"Invalid response. Choose your dietary requirement from the following options, or press enter if none\n{diet}: ")
    diet_flag = 0
if diet_choice == "":
    diet_flag = 0
elif diet_choice in diet:
    includediet = f'Diet ={diet_choice}'
    diet_flag = 1

print("\033[1m Fetching Recepies ... \033[0;0m")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
import sys
import time
for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

# pulls API parameters into the url based on user choices, and sets relevant print message for each combo
if diet_flag == 1 and cuisine_flag == 1:
    url = f'https://api.edamam.com/search?{includeIngredients}&{includeAppId}&{includeAppKey}&{includediet}&{includecuisine}'
    recipeChoices = f'You searched for {cuisine_choice} and {diet_choice} recipe options, using {components} '

elif diet_flag == 0 and cuisine_flag == 1:
    url = f'https://api.edamam.com/search?{includeIngredients}&{includeAppId}&{includeAppKey}&{includecuisine}'
    recipeChoices = f'You searched for {cuisine_choice} recipe options, using {components} '

elif diet_flag == 1 and cuisine_flag == 0:
    url = f'https://api.edamam.com/search?{includeIngredients}&{includeAppId}&{includeAppKey}&{includediet}'
    recipeChoices = f'You searched for {diet_choice} recipe options, using {components} '

elif diet_flag == 0 and cuisine_flag == 0:
    url = f'https://api.edamam.com/search?{includeIngredients}&{includeAppId}&{includeAppKey}'
    recipeChoices = f'You searched for recipe options, using {components} '


# requests and extracts recipes from the API, into the 'results' variable, based on user choices above
results = requests.get(url)
data = results.json()
results = data['hits']

# Printing the results
print("\n ")
print(recipeChoices)
# loops through results and adds 1 on each iteration (to count how many results found)
count = 0
for result in results:
    recipe = result['recipe']
    count = count + 1
if count > 0:
    print('Here are your recipes: ')
else:
    print("\n ")
    print('Sorry, no recipes found!')

# loops through results again, where more than 0 results found...
for result in results:
    recipe = result['recipe']
     # define recipe info variables, i.e. name, web link, servings, nutrition, total time, and ingredients list
    recipeLabel = recipe['label']
    webLink = recipe['url']
    calories = round(int(recipe['calories'] / recipe['yield']))


    y = round(int(recipe['yield']))
    ingredList = recipe['ingredientLines']
    time = round(int(recipe['totalTime']))
    # prints recipe name, web link, servings, and nutrition info
    print("\n")
    print(recipeLabel)
    print(webLink)
    print( str(y) + ' servings')
    print('Calories per serving: ' + str(calories) + ' calories ' )
    # not all recipes include total time, so prints this info only if they do (i.e. total time is more than 0 minutes)
    if time > 0:
        print('Preparation time: approximately ' + str(time) + ' minutes')
    else:
        pass


print("\n")
# if more than one recipe found, asks user to choose a recipe and prints/saves shopping (ingredients) list to a text file
if count > 0:
    chosen_recipe = input('What recipe would you like to cook?: ')
    if chosen_recipe == recipeLabel:
        MyFile = open('Food recepies.txt', 'a')
        MyFile.write('\n\033[1m'+ f'Food recepie: {recipeLabel} ({y} servings) '+ '\033[0;0m')
        MyFile.write('\n\n')
        for i in range(0, len(ingredList)):
            MyFile.write(ingredList[i])
            MyFile.write('\n')
        MyFile.write(f'(Link to recipe: {webLink})\n')
        MyFile.close()
        # prints final message to user, confirming shopping list file has been saved and asking if they want to open/print it
        print(f'Your recepie for {recipeLabel} has been saved.')
        with open('Food recepies.txt', 'r') as text_file:
            contents = text_file.read()
            print(contents)
    else:
        pass
else:
    pass
