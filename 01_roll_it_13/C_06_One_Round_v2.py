import random


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
    winner ="user"

else:
    winner = "computer"

round_feedback = f" the {winner} won."

if winner == "user" and double_user == "yes":
    user_points = user_points * 2

make_statement(statement= "Round Results", decoration= "=")
print(f"User Points: {user_points} | Computer Points: {comp_points}")
print(round_feedback)
print()