
import requests
i = 1

# API Items
apiKey = "8829ae0dd51a4ad693495a811663a202"
url_one = "https://api.spoonacular.com/recipes/findByIngredients"
url_two = "https://api.spoonacular.com/food/ingredients/substitutes"


# ONE: Fetch recipes based on available ingredients
available = input("What Ingredients do you have in your fridge? (list with commas separating ingredients)")
params = {
    "ingredients": available,
    "apiKey": apiKey,
    "number": 3
}

recipes = requests.get(url_one, params)
recipe_array = recipes.json()

# Suggest 3 recipes
recipeStore = {}
for recipe in recipe_array:
    # Recipe Titles
    print("Recipe", i, ": ", recipe["title"])
    recipeStore[i] = recipe["id"]
    i += 1
    # Ingredients
    Ingredients = []
    for k in range(len(recipe["usedIngredients"])):
        Ingredients.append(recipe["usedIngredients"][k]["name"])
    for j in range(len(recipe["missedIngredients"])):
        Ingredients.append(recipe["missedIngredients"][j]["name"])

    print("All the Necessary Ingredients are: ", Ingredients)


# TWO: select recipe and display instructions
chosen = input("Which recipe number would you like to explore further?")

id = recipeStore[int(chosen)]
url_three = "https://api.spoonacular.com/recipes/"+str(id)+"/analyzedInstructions"
params_three = {
        "id": id,
        "apiKey": apiKey
    }

instruct = requests.get(url_three, params_three)
data_instruct = instruct.json()

howTo = {}
for steps in data_instruct:
    # PRINT steps-->equipment-->name, steps-->ingredients-->name, steps-->number, steps-->step
    for x in range(len(steps["steps"])):
        howTo.append(steps["steps"]["equipment"][x]["name"])
    for y in range(len(steps["steps"])):
        howTo.append(steps["steps"]["ingredients"][y]["name"])



# THREE: substitute ingredients
subs = input("Need to substitute an ingredient?")
params_two = {
        "ingredientName": subs,
        "apiKey": apiKey
    }

swap_ing = requests.get(url_two, params_two)
data_swap = swap_ing.json()
print(data_swap)

