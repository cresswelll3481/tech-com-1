# make a welcome message
def statement_generator(statement):
    print(f"{statement}")


def instructions():
    statement_generator("instructions")
    print('''
Instructions go here.

        ''')


# Main rouitne goes here
want_instructions = input("press <enter> to read the instructions or any key to continue.")


instructions()



print("program continues")
