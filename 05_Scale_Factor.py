# Ingredients list


#
# Number Checking Function
def num_check(question):

    error = "please enter a number that is more than zero"

    valid = False
    while not valid:
        response = (input(question))

        if response.lower() == "xxx":
            return "xxx"

        else:
            try:
                if float(response) <= 0:
                    print(error)
                else:
                    return response

            except ValueError:
                print(error)
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

scale_Factor = float(input("Scale Factor: "))

# Set up empty ingredient list
Ingredients = []
# Loop to ask users to enter an ingredient
stop = ""
while stop != "xxx":

    amount = num_check("What is the amount for the ingredient? ")

    # If exit code is typed...
    if amount.lower() == "xxx" and len(Ingredients) > 1:
        break
    # Check that list contains at least two items
    elif amount.lower() == "xxx" and len(Ingredients) <2:
        print("You need at least two ingredients in the list. "
              "Please add more ingredients. ")
        continue

# If exit code is not entered, add to ingredient list
    else:
        # Ask user for ingredient (Via not blank function)
        get_Ingredient = not_blank("Please type in an ingredient name: ",
                                   "This cant be blank",
                                   "yes")
        amount = float(amount) * scale_Factor

        Ingredients.append("{} units {}".format(amount, get_Ingredient))

# Output list
print(Ingredients)