# Conversion Function...

import csv

# ****** Functions go here ******
def general_converter(how_much, lookup, dictionary, conversion_factor ):

    if lookup in dictionary:
        mult_by = dictionary.get(unit)
        how_much = how_much * float(mult_by) / conversion_factor
        converted = "yes"

    else:
        converted = "no"

    return [how_much, converted]

def unit_checker(raw_unit):

    unit_tocheck = input("Unit? ")

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

groceries = open('01_ingredients_ml_to_g.csv')

csv_groceries = csv.reader(groceries)

food_dictionary = {}

for row in csv_groceries:
    food_dictionary[row[0]] = row [1]

print(food_dictionary)

keep_going = ""
while keep_going == "":
    amount = eval(input("How much? "))
    amount = float(amount)

    unit = unit_checker()
    ingredient = input("Ingredient: ")

    amount = general_converter(amount, unit, unit_central, 1)
    print(amount)

    if amount[1] == "yes":
        amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

        if amount_2[1] == "yes":
            print(amount_2)

        else: print("unchanged")

    else:
        print("unchanged")

    # keep_going = input("<enter> or q ")
