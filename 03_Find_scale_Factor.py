# To Do

# Ask user for servings made by recipe (and check this is an number that is more that 4)
# Ask user for servings desired (check this is a number)
# Calculate the scale factor
# Warn the user if the sf is less than 0.25 or more than 4

# Functions go here
def num_check(question):

    error = "please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            reponse = float(input(question))

            if reponse <= 0:
                print(error)
            else:
                return reponse

        except ValueError:
            print(error)

# Main Routine goes here
sf_ok = "no"
while sf_ok == "no":

    serving_size = num_check("What is the recipe serving size? ")
    desired_size = num_check("How many servings are needed?")

    scale_factor = desired_size / serving_size

    if scale_factor < 0.25:
        sf_ok = input("Warning: this scale factor is very small"
                      "and you might struggle to accurately Weigh"
                      "the ingredients. \n"
                      "Do you want to keep going (type 'no' to change"
                      "you desired serving size or 'yes' to keep it how it is").lower()
    elif scale_factor > 4:
        sf_ok = input("Warning: this scale factor is quite large"
                      "and you might struggle with mixing bowl/oven space. \n"
                      "Do you want to keep going (type 'no' to change"
                      "you desired serving size or 'yes' to keep it how it is)").lower()
    else:
        sf_ok = "yes"

print("Scale Factor: {}".format(scale_factor))