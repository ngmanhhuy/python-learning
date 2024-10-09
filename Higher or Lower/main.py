import random
from art import logo, vs
from game_data import data

def print_choices(a, b):
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")

def is_correct(a, b, choice):
    if a['follower_count'] > b['follower_count']:
        return choice == 'a'
    else:
        return choice == 'b'

def higher_or_lower():
    print(logo)
    game_over = False
    score = 0
    choice_a = random.choice(data)
    choice_b = random.choice(data)
    while choice_b == choice_a:
        choice_b = random.choice(data)

    while not game_over:
        print_choices(choice_a, choice_b)
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if is_correct(choice_a, choice_b, user_choice):
            score += 1
            print(f"Correct! Your current score: {score}")
            if user_choice == 'b':
                choice_a = choice_b
            current_b = choice_b
            while choice_b == current_b or choice_b == choice_a:
                choice_b = random.choice(data)
        else:
            game_over = True

    if game_over:
        print(f"Oops... You lose! Final score is: {score}")
        print(f"{choice_a['name']} has {choice_a['follower_count']} million followers")
        print(f"{choice_b['name']} has {choice_b['follower_count']} million followers")

higher_or_lower()