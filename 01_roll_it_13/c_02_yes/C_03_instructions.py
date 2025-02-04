def yes_no(question):
    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes or no")


    #main

def instructions():
     print("""
    ***** Instructions *****
       
    Roll the die and try to win
         """)

want_instructions = yes_no("Do you want to see the instructions. ").lower()

if want_instructions == "yes":
    instructions()

print()
print("program continues")