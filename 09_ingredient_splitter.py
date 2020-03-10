import re

# ingredient has mixed fraction followed by unit and ingredient
full_recipe =[
    "1 1/2 ml flour",
    "3/4 cup milk",
    "1 cup flour",
    "2 teaspoons white sugar",
    "pinch of cinnamon"
]
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()
    # Get amount...
    if re.match(mixed_regex, recipe_line):

        # Get mixed number by matching the regex+
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
        get_amount = recipe_line.split("", 1)

        try:
            amount = eval(get_amount[0])
        except NameError:
            amount = get_amount[0]
            convert = "no"

        unit_ingredient = get_amount[1]

get_unit = unit_ingredient.split("", 1)
unit = get_unit[0]
ingredient = get_unit[1]

print("{} {} {}".format(amount, unit, ingredient))