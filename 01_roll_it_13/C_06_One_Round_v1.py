import random

user_points = 0
comp_points = 0
double_user = "no"

user_one = random.randint(1, 6)
user_two = random.randint(1, 6)

if user_one == user_two:
    double_user = "yes"

comp_one = random.randint(1, 6)
comp_two = random.randint(1, 6)


user_points += user_one + user_two
comp_points += comp_one + comp_two

print("\nInital points")
print(F"user   - Roll 1: {user_one} \t| Roll 2: {user_two} \t| Total: {user_points}")
print(F"computer   - Roll 1: {comp_one} \t| Roll 2: {comp_two} \t| Total: {comp_points}")

if double_user == "yes":
    print("Great news  if you win then you will earn double points")