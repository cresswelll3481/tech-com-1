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

def int_check():
    error = "please enter an integer more than / equal to 13."

    while True:
        try:
            response = int(input("what is the game goal? "))


            if response < 13:
                print(error)

            else:
                return response

        except ValueError:
            print(error)

want_instructions = yes_no("Do you want to see the instructions. ").lower()

if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()
print(game_goal)