
game_history = []

user_score = 0
comp_score = 0

while True:

    rounds_played = input("Round? ")
    if rounds_played == "":
        break

    user_points = int(input("user points? "))
    comp_point = int(input("computer points? "))
    winner = input("who won? ")
    user_score = int(input("user score: "))
    comp_score = int(input("comp score: "))


    game_result = (f"round {rounds_played}: User points {user_score} | " 
                  f"computer points {comp_point}, {winner} ({user_score}| {comp_score})")

    game_history.append(game_result)

print("game history")

for item in game_history:
    print(item)