import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    print(f"> You drew a card: {card}")
    return card

def calculate_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🤝"
    elif c_score == 0:
        return "You lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Blackjack! You win 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    print("\n" + "=" * 35)
    print("         NEW BLACKJACK GAME         ")
    print("=" * 35)

    # Initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f"\nYour starting cards: {user_cards}")
    print(f"Computer's visible card: [{computer_cards[0]}, ?]")

    while not is_game_over:
        user_score = calculate_cards(user_cards)
        computer_score = calculate_cards(computer_cards)

        print(f"\nYour hand: {user_cards} | Your score: {user_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to draw another card, or 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        print("\nComputer draws a card...")
        computer_cards.append(deal_card())
        computer_score = calculate_cards(computer_cards)
        print(f"Computer's current hand: {computer_cards} | Score: {computer_score}")

    print("\n" + "-" * 35)
    print("              FINAL RESULT           ")
    print("-" * 35)
    print(f"Your final hand:     {user_cards} | Final score: {user_score}")
    print(f"Computer's final hand: {computer_cards} | Final score: {computer_score}")
    print("\n" + compare(user_score, computer_score))
    print("-" * 35)

# Main game loop
while input("\nDo you want to play Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()

###calculate
# def calculate_cards(cards):
#     if sum(cards) == 21 and len(cards) ==2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)
