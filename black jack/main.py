import random
from art import logo

# Predefined card deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """
    Returns a random card from the predefined deck.

    Returns:
        int: A randomly chosen card value from the list 'cards'.
    """
    return random.choice(cards)


def check_blackjack(hands):
    """
    Checks if the given hand is a blackjack (Ace and 10-value card).

    Args:
        hands (list): List of integers representing the player's or computer's hand.

    Returns:
        bool: True if the hand contains a blackjack, False otherwise.
    """
    return 11 in hands and 10 in hands


def count_score(hands):
    """
    Calculates the total score of a hand and adjusts the score for Ace (11) if the score exceeds 21.

    Args:
        hands (list): List of integers representing the player's or computer's hand.

    Returns:
        int: The total score of the hand.
    """
    score = sum(hands)
    if score > 21 and 11 in hands:
        hands[hands.index(11)] = 1  # Replace one Ace (11) with 1 to avoid bust
        score = sum(hands)
    return score


def print_hand(user_hand, computer_hand, reveal_computer=False):
    """
    Prints the current hand and scores for the user and the computer. If 'reveal_computer' is False, only shows the first card of the computer's hand.

    Args:
        user_hand (list): List of integers representing the user's hand.
        computer_hand (list): List of integers representing the computer's hand.
        reveal_computer (bool): If True, reveals the computer's full hand and score. Defaults to False.
    """
    user_score = count_score(user_hand)
    print(f"Your cards: {user_hand}, current score: {user_score}")

    if reveal_computer:
        computer_score = count_score(computer_hand)
        print(f"Computer's cards: {computer_hand}, current score: {computer_score}")
    else:
        print(f"Computer's first card: {computer_hand[0]}")


def compare(user_score, computer_score):
    """
    Compares the scores of the user and the computer to determine the winner.

    Args:
        user_score (int): The total score of the user's hand.
        computer_score (int): The total score of the computer's hand.

    Returns:
        str: A message indicating the outcome of the game (win, lose, or draw).
    """
    if user_score == computer_score:
        return "Draw!"
    elif user_score > 21:
        return "You went over 21! You lose!"
    elif computer_score > 21:
        return "Computer went over 21! You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def blackjack():
    """
    Main function to run a single game of Blackjack.
    Handles dealing cards, user interaction, and comparing the results.
    """
    print(logo)
    user_hand = [deal_card() for _ in range(2)]
    computer_hand = [deal_card() for _ in range(2)]

    # Initial hands print
    print_hand(user_hand, computer_hand)

    # Check for initial blackjack
    if check_blackjack(computer_hand):
        print("Computer has blackjack!")
        print_hand(user_hand, computer_hand, reveal_computer=True)
        return
    elif check_blackjack(user_hand):
        print("You have blackjack!")
        print_hand(user_hand, computer_hand, reveal_computer=True)
        return

    # User turn
    while count_score(user_hand) < 21:
        user_choice = input("Type 'y' to hit another card, type 'n' to pass: ")
        if user_choice == 'y':
            user_hand.append(deal_card())
            print_hand(user_hand, computer_hand)
        else:
            break

    user_score = count_score(user_hand)
    if user_score > 21:
        print(compare(user_score, count_score(computer_hand)))
        return

    # Computer turn
    while count_score(computer_hand) < 17:
        computer_hand.append(deal_card())

    computer_score = count_score(computer_hand)

    # Final hand print and result
    print_hand(user_hand, computer_hand, reveal_computer=True)
    print(compare(user_score, computer_score))


# Game loop
want_to_play = True
while want_to_play:
    choice = input("Do you want to play blackjack? (y/n): ")
    if choice == 'y':
        print('\n' * 20)
        blackjack()
    else:
        want_to_play = False
        print("Goodbye!")