def yes_no(question):
    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "yes"
        else:
            print("please enter yes or no")


    #main
want_instructions = yes_no("Do you want to see the instructions. ").lower()
want_coffee = yes_no("do you want coffee.   ")
print("we done")