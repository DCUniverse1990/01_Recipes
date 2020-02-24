def check(question):

    error = "please enter a number that is more than zero"

    try:
        response = float(input(question))

        if response <= 0:
                print(error)

        else:
            return response

    except ValueError:
        print(error)

sf_ok = "no"
while sf_ok == "no":

    serving_size = check("What is the recipe serving size? ")
    desired_size = check("How many servings are needed?")
    sf_ok = "yes"


print(serving_size)
print(desired_size)