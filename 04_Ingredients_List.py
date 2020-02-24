# Ingredients list


# Not blank Function goes here
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


# Main Routine goes here

# Main Routine...

# Set up empty ingredient list
Ingredients = []
# Loop to ask users to enter an ingredient
stop = ""
while stop != "xxx":
    # Ask user for ingredient (Via not blank function)
    get_Ingredient = not_blank("Please type in an ingredient name: ",
                               "This cant be blank",
                               "yes")
    # If exit code is typed...
    if get_Ingredient.lower()=="xxx" and len(Ingredients) > 1:
        break
# Check that list contains at least two items

# If exit code is not entered, add to ingredient list
    else:
        Ingredients.append(get_Ingredient)
# Output list
print(Ingredients)