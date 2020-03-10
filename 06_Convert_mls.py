# ask user for amount
# ask user for unit
# check that unit is in dictionary

# if unit in dictionary, convert to mL

# if no unit given / unit is unknown, leave as is.


# ****** Funtions go here ******
def unit_checker():

    unit_tocheck = input("Unit? ")

    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]

    if unit_tocheck == "":
        print("You chose {}".format(unit_tocheck))
        return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"

# ******* Main routine goes here *******
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 30,
    "pint": 473,
    "quart": 946,
    "pound": 454
}

keep_going = ""
while keep_going == "":
    amount = eval(input("How much? "))
    amount = float(amount)

    unit = unit_checker()

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount in ml {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    keep_going = input("<enter> or q ")