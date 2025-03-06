import random


def yes_no(question):
    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes or no")

    # main


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
def inital_points(which_player):
    double = "no"

    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(F"{which_player}   - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total}")

    return total, double

def make_statement(statement, decoration):

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")



comp_score = 0
user_score = 0
rounds_played = 0

game_history = []

make_statement(statement= "Welcome To The Roll It 13 Game", decoration= "_")
want_instructions = yes_no("Do you want to see the instructions. ").lower()

if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()


while comp_score < game_goal and user_score < game_goal:

    rounds_played += 1

    make_statement(statement= f"Rounds played  {rounds_played}", decoration=  "*")


    initial_user = inital_points("user")
    initial_comp = inital_points("comp")


    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    if double_user == "yes":
        print("Great news  if you win then you will earn double points")

    first  =  "user"
    second = "computer"
    player_1_points = user_points
    player_2_points = comp_points

    if user_points < comp_points:
        print("you start because your initial roll was less than that computer\n")

    elif user_points == comp_points:
        print("the initial rolls were the same, the user starts")

    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    while player_1_points < 13 and player_2_points < 13:
        print()
        input("press <enter> to continue this round")
        print()

        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: rolled a {player_1_roll} - has  {player_1_points} points")

        if player_1_points >= 13:
            break

        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll
        print(f"{second}: rolled a {player_2_roll} - has  {player_2_points} points")

        print(f"{first}:  {player_1_points} | {second}  {player_2_points}")


    user_points = player_1_points
    comp_points = player_2_points

    if first == "computer":
        user_points, comp_points = comp_points, user_points

    if user_points > comp_points:
        winner = "User"
        loser = "Computer"
        comp_points = 0

    else:
        winner = "Computer"
        loser = "User"
        user_points = 0

    round_feedback = f" the {winner} won."

    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    make_statement(statement= "Round Results", decoration= "=")
    print(f"User Points: {user_points} | Computer Points: {comp_points}")
    print(round_feedback)
    print()


    comp_score += comp_points
    user_score += user_points

    game_result = (f"round {rounds_played}: User points {user_points} | " 
                  f"computer points {comp_points}, {winner}"
                   f" ({user_score}| {comp_score})")

    game_history.append(game_result)

    print("*** Game Update ***")
    print(f"User Score: {user_score} | Computer Score {comp_score} ")

    make_statement(statement= "Game Over", decoration= "#")

    print()
    if user_score > comp_score:
        make_statement(statement="The User Won", decoration="*")

    else:
        make_statement(statement="The Computer Won", decoration="+")


make_statement(statement="Game History", decoration="=")

for item in game_history:
    print(item)
