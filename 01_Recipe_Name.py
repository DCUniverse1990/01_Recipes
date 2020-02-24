# Get's recipe name and checks it is not blank

# Not Blank Function goe here
def not_blank(question):
    error = "you have a number in your named recipe."

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        # look at each character in sting and if its a number, complain
        for letter in response:
            if letter.isdigit() == True:
                has_errors = "yes"
                continue

        if response == "":
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# Main Routine goes here

recipe_name = not_blank("What is the recipe name? ")

print("You are making {}".format(recipe_name))