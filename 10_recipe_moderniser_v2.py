# modules to be used...
import csv
import re

# ***** Functions ******

# make that it so there can not be blanks
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in sting and if its a number, complain
                for letter in response:
                    if letter.isdigit() == True:
                        has_errors = "yes"
                        break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response

# check that number is available
def num_check(question):

    error = "please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# get scale factor
def get_sf():
    serving_size = num_check("What is the recipe serving size? ")

    sf_ok = "no"
    while sf_ok == "no":

        desired_size = num_check("How many servings are needed?")

        sf = desired_size / serving_size

        if sf < 0.25:
            sf_ok = input("Warning: this scale factor is very small"
                          "and you might struggle to accurately Weigh"
                          "the ingredients. \n"
                          "Do you want to keep going (type 'no' to change\n"
                          "your desired serving size or 'yes' to keep it how it is").lower()
        elif sf > 4:
            sf_ok = input("Warning: this scale factor is quite large"
                          "and you might struggle with mixing bowl/oven space. \n"
                          "Do you want to keep going (type 'no' to change "
                          "your desired serving size or 'yes' to keep it how it is)").lower()
        else:
            return sf

# ask user for ingredients
def get_all_ingredients():
    all_ingredients = []

    stop = ""
    while stop != "xxx":
        # Ask user for ingredient (Via not blank function)
        get_recipe_line = not_blank("Recipe line: ",
                                   "This cant be blank",
                                   "yes")
        # If exit code is typed...
        if get_recipe_line.lower() == "xxx" and len(all_ingredients) > 1:
            break

        elif get_recipe_line.lower() == "xxx" and len (all_ingredients) <2:
            print("you need at least too ingredients in the list. "
                  "Please add more ingredients.")

            # If exit code is not entered, add to ingredient list
        else:
            all_ingredients.append(get_recipe_line)

    return all_ingredients


def general_converter(how_much, lookup, dictionary, conversion_factor ):

    if lookup in dictionary:
        mult_by = dictionary.get(lookup)
        how_much = how_much * float(mult_by) / conversion_factor
        converted = "yes"

    else:
        converted = "no"

    return [how_much, converted]

# check that unit is available
def unit_checker(unit_tocheck):

    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]
    ounce = ["oz", "ounce", "fl oz"]
    cup = ["c", "cup"]
    pint = ["p", "pt", "fl qt"]
    quart = ["q", "qt", "fl qt"]
    mls = ["ml", "milliliter"]
    litre = ["litre", "liter", "l"]
    pound = ["pound", "lb", "#"]

    if unit_tocheck == "":
        print("You chose {}".format(unit_tocheck))
        return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in mls:
        return "mL"
    elif unit_tocheck.lower() in litre:
        return "Litre"
    elif unit_tocheck.lower() in pound:
        return "pound"

# ******* Main routine goes here *******

# Set up Dictionaries

#  ***** UNITS DICTIONARY *****
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 30,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000,
    "ml": 1
}


#  ******  INGREDIENTS DICTIONARY *******
groceries = open('01_ingredients_ml_to_g.csv')

csv_groceries = csv.reader(groceries)

food_dictionary = {}

for row in csv_groceries:
    food_dictionary[row[0]] = row [1]

print(food_dictionary)

# set up list to hold 'modernised' ingredients
moderniser_recipe = []

# *****  GET USER INPUT.... *****

# Ask for recipe name and source
recipe_name = not_blank("What is the recipe name? ",
                   "The recipe source can't be blank and cant contain numbers",
                   "no")

# ask user where the recipe is originally from (numbers OK)
source = not_blank("Where is the recipe from? ",
                   "The recipe source can't be blank",
                   "yes")

# Get serving sizes and scale factor
scale_factor = get_sf()

# Ask User for Ingredients
full_recipe = get_all_ingredients()

# Loop for each ingredient...
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

new_line=""

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()
    # Get amount...

    # if amount is a mixed number, convert it to a decimal
    if re.match(mixed_regex, recipe_line):

        # Get mixed number by matching the regex
        pre_mix_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mix_num.group()

        # Replace space with a + sign...
        amount = mixed_num.replace(" ", "+")
        # Change the string into a decimal
        amount = eval(amount)

        # Get unit and ingredient..
        compile_regex = re.compile(mixed_regex)
        print(compile_regex)
        unit_ingredient = re.split(compile_regex, recipe_line)
        unit_ingredient = (unit_ingredient[1]).strip()

    else:
        get_amount = recipe_line.split(" ", 1)

        try:
            amount = eval(get_amount[0])
            amount = amount * scale_factor

        except NameError:
            amount = get_amount[0]
            moderniser_recipe.append(recipe_line)
            continue

        unit_ingredient = get_amount[1]

    get_unit = unit_ingredient.split(" ", 1)
    num_spaces = recipe_line.count(" ")

    # print modernised recipe
    if num_spaces > 1:
        unit = get_unit[0]
        ingredient = get_unit[1]
        unit = unit_checker(unit)

        if unit == "g":
            new_line = "{:.0f} g {}".format(amount, ingredient)
            continue

        amount = general_converter(amount, unit, unit_central, 1)
        if amount[1] == "yes":
            amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

            if amount_2[1] == "yes":
                moderniser_recipe.append("{:.0f} g {}".format(amount_2[0], ingredient))

            else:
                moderniser_recipe.append("{:.0f} g {}".format(amount_2[0], ingredient))
                continue

        else:
            moderniser_recipe.append("{} {} {}".format(amount, unit_ingredient, ingredient))
            continue

for item in moderniser_recipe:
    print(item)


