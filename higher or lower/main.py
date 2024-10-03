import random
from art import logo, vs
from game_data import data

def print_choices(a, b):
    print(f"Compare A: {a.get('name')}, {a.get('description')}, from {a.get('country')}")
    print(vs)
    print(f"Against B: {b.get('name')}, {b.get('description')}, from {b.get('country')}")

def is_correct(a, b, choice):
    if a.get('follower_count') > b.get('follower_count') and choice == 'a':
        return True
    elif a.get('follower_count') < b.get('follower_count') and choice == 'b':
        return True
    else:
        return False

def higher_or_lower():
    print(logo)
    game_over = False
    score = 0
    choice_a = random.choice(data)
    choice_b = random.choice(data)
    if choice_a == choice_b:
        choice_b = random.choice(data)

    while not game_over:
        print_choices(choice_a, choice_b)
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if is_correct(choice_a, choice_b, user_choice):
            score += 1
            print(f"Correct! Your current score: {score}")
            if user_choice == 'b':
                choice_a = choice_b
            choice_b = random.choice(data)
            if choice_a == choice_b:
                choice_b = random.choice(data)
        else:
            game_over = True

    if game_over:
        print(f"Oops... You lose! Your score is: {score}")
        print(f"{choice_a.get('name')} has {choice_a.get('follower_count')} million followers")
        print(f"{choice_b.get('name')} has {choice_b.get('follower_count')} million followers")

higher_or_lower()